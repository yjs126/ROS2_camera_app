from setuptools import find_packages, setup
import glob
import os

package_name = 'camera_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob.glob(os.path.join('param', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='addinedu',
    maintainer_email='yjs126@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = camera_package.img_publisher:main',
            'canny_edge = camera_package.canny_edge:main',
            'optical_flow = camera_package.optical_flow:main',
            'img_capture_service_server = camera_package.img_capture_service_server:main'
        ],
    },
)
