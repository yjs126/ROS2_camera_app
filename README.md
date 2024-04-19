# ROS2 camera app project
---

## Instroduction

This package is a project that implements the functionality of camera application with ros2 Humble  
The usage environment is unbuntu 22.04

---
## Overview
![Screenshot from 2024-04-19 16-28-19](https://github.com/yjs126/ROS2_camera_app/assets/156267935/f2967c6f-a558-4b51-a405-1f0d35b59148)

![Screenshot from 2024-04-19 17-48-42](https://github.com/yjs126/ROS2_camera_app/assets/156267935/d02fc9fb-ce54-46cd-a719-38323c7ffd08)

---
## Install         

- step1  
Create a "camera_ws" folder (You can change the workspace name)
- step2  
Create album, src folder below  
![Screenshot from 2024-04-19 16-59-10](https://github.com/yjs126/ROS2_camera_app/assets/156267935/53ad8bb0-6451-4b45-aefa-aa65f9966693)
- step3  
Go to "/camera_ws" path
- step4  
Build on the workspace path
<pre>
  <code>
    yourpc@yourid:~/../camera_ws$ colcon build
  </code>
</pre>
- step5  
"Build", "install", "log" folders are created  
![Screenshot from 2024-04-19 17-05-14](https://github.com/yjs126/ROS2_camera_app/assets/156267935/6abddcf7-2de5-4e88-8a10-6edb13d46a6d)
---
## Use Manual
#### 1. To bring up the ros2 environment, run setup.bash
<pre>
  <code>
    yourpc@yourid:~$ source ~/../camera_ws/install/local_setup.bash
  </code>
</pre>
#### 2. Launch camera.launch.py file
<pre>
  <code>
    yourpc@yourid:~/../camera_ws$ ros2 launch camera_package camera.launch.py
  </code>
</pre>
#### 3. Open "rqt" Image View
   
#### 4. Select camera filter topic
- /camera : origin frame
- /img_canny : canny edge filter apply
- /img_optical : optical filter apply
#### 5. Input command for capture,recording
- cap : image capture
- rec : start recording
- stop : stop recording
<pre>
  <code>
    yourpc@yourid:~/../camera_ws$ ros2 service call /img_capture camera_package_msgs/srv/Capture {"mode: cap"}

    yourpc@yourid:~/../camera_ws$ ros2 service call /img_capture camera_package_msgs/srv/Capture {"mode: rec"}

    yourpc@yourid:~/../camera_ws$ ros2 service call /img_capture camera_package_msgs/srv/Capture {"mode: stop"}
  </code>
</pre>
---

