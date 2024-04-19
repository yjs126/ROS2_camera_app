from camera_package_msgs.srv import Capture

import cv2
import numpy

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import datetime

class ImgCapture(Node):
    def __init__(self):
        super().__init__('img_capture_service_server')

        self.recFlg = False
        self.isRecStart = False

        # self.declare_parameter('width', 640)
        # self.width = self.get_parameter('width').value
        # self.declare_parameter('length', 480)
        # self.length = self.get_parameter('length').value

        self.server = self.create_service(Capture,'/img_capture',self.callback_service)

        self.declare_parameter('path', '/home/addinedu/ros2/camera_ws/album/')
        self.path = self.get_parameter('path').value

        self.img_subscriber = self.create_subscription(Image,'/camera', self.img_callback,10)
        self.canny_subscriber = self.create_subscription(Image,'/img_canny', self.canny_callback,10)
        self.optical_subscriber = self.create_subscription(Image,'/img_optical', self.optical_callback,10)
        

        self.timer = self.create_timer(0.05, self.videoRecord)
        self.cv_bridge = CvBridge()


    def callback_service(self, request, response):
        self.cannySubCount = self.count_subscribers('/img_canny')
        self.opticalSubCount = self.count_subscribers('/img_optical')
        print("canny count : ", self.count_subscribers('/img_canny') )
        print("optical count : ", self.count_subscribers('/img_optical') )

        self.mode = request.mode

    
        print("service callback!!!!!!!!!!!!!")

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        self.img_filename = self.path + now + ".png"
        self.video_filename = self.path + now + ".avi"

        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")

        w = 320
        h = 240
        # print(self.width, self.length)
        
        
        if self.cannySubCount > 1:
            print("canny")
            self.img = self.img_canny
        elif self.opticalSubCount > 1:
            print("optical")
            self.img = self.img_optical
        else:
            print("origin")
            self.img = self.img_origin


        if self.mode=='cap':
            cv2.imwrite(self.img_filename, self.img)
        elif self.mode=='rec':
            self.recFlg = True
            self.writer = cv2.VideoWriter(self.video_filename, self.fourcc, 20.0, (w, h))
        elif self.mode=='stop':
            self.recFlg = False
        else:
            pass


        return response
        
        
    def img_callback(self, msg):
        self.img_origin = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def canny_callback(self, msg):
        self.img_canny = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def optical_callback(self, msg):
        self.img_optical = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')


    def videoRecord(self):
        # 선택된 토픽이 캐니인지 어쩐지
        if self.recFlg==True:
            if self.cannySubCount > 1:
                frame = self.img_canny
            elif self.opticalSubCount > 1:
                frame = self.img_optical
            else:
                frame = self.img_origin

            self.writer.write(frame)
        else:
            if self.isRecStart==True:
                print("stopping")
                self.isRecStart = False
                self.writer.release()
            else:
                pass
                  

def main():
    rclpy.init()
    node = ImgCapture()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()