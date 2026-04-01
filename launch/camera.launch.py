import os
from pathlib import Path
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from camera_config import CameraConfig, USB_CAM_DIR
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    camera = CameraConfig(
        name="camera",
        param_path=Path(USB_CAM_DIR, 'config', 'camera_ros_params.yaml'),
    )

    return LaunchDescription(
        [
            Node(
                package="usb_cam",
                executable="usb_cam_node_exe",
                name=camera.name,
                output="screen",
                namespace=camera.namespace,
                parameters=[str(camera.param_path)],
                remappings=camera.remappings,
            )
        ]
    )
