#!/usr/bin/env python3

from setuptools import setup

package_name = 'gazebo_differential_drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools','pyserial'],
    zip_safe=True,
    maintainer='simenza',
    maintainer_email='simenza@example.com',
    description='Differential drive robot with Gazebo and ROS 2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'odom_to_tf = gazebo_differential_drive_robot.odom_to_tf:main',
            'lidar_read_node = gazebo_differential_drive_robot.lidar_read_node:main'
        ],
    },
)
