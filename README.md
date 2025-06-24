# KitchenBot
ROS2 Humble based differential drive robot simulated in Gazebo Ignition.

Prerequisites:
- ROS 2 Humble
- Gazebo Ignition
- slam_toolbox plugin
- nav2 plugin

How to use (after cloning the repo on your workspace):
1. ros2 launch gazebo_differential_drive_robot robot.launch.py
2. ros2 launch slam_toolbox online_async_launch.py slam_params_file:=(path_to_your_ws)/gazebo_differential_drive_robot/config/mapper_params_online_async.yaml use_sim_time:=true
3. ros2 launch nav2_bringup navigation_launch.py params_file:=(path_to_your_ws)/gazebo_differential_drive_robot/config/nav2_params.yaml use_sim_time:=true
4. rviz2 (just for visualization)
5. ros2 run naoqi_driver send_goal.py
6. ros2 run naoqi_driver create_request.py
7. ~/(path_to_your_ws)/gazebo_differential_drive_robot/gazebo_differential_drive_robot/interface$ python3 server.py 
