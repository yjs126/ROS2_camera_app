import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description(): 
    param_cam = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('camera_package'),
        'param',
        'size.yaml')
        )
    
    param_filter = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('camera_package'),
        'param',
        'filter.yaml')
        )
    
    param_path = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('camera_package'),
        'param',
        'saveDirectory.yaml')
        )
    
    return LaunchDescription(
        [
            DeclareLaunchArgument( 
                'param_dir',
                default_value=param_cam
            ),

            Node(
                package='camera_package',
                executable='img_publisher',
                name='img_publisher',
                parameters=[param_cam],
                output='screen'),

            Node(
                package='camera_package',
                executable='canny_edge',
                name='canny_edge',
                parameters=[param_filter],
                output='screen'),

            Node(
                package='camera_package',
                executable='optical_flow',
                name='optical_flow',
                parameters=[param_filter],
                output='screen'),

            Node(
                package='camera_package',
                executable='img_capture_service_server',
                name='img_capture_service_server',
                parameters=[param_cam, param_path],
                output='screen'),
        ]
    )