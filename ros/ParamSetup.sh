#!/bin/bash
set -x

rosparam set tf_x 1.2
rosparam set tf_y 0.0
rosparam set tf_z 2.0
rosparam set tf_yaw 0.0
rosparam set tf_pitch 0.0
rosparam set tf_roll 0.0
rosparam set localizer velodyne
rosparam set /use_sim_time false

echo "Finish Parameter Setting"

#Each of the following should be done in a separate terminal
#1. roscore && bash commandLineStarter.sh
#2. rosbag play ~/.autoware/new_spec.bag (hit space to pause immediately)
#3. roslaunch ~/.autoware/my_launch/my_map.launch
#4. roslaunch ~/.autoware/my_launch/my_localization.launch
#5. roslaunch ~/.autoware/my_launch/my_mission_planning.launch
#6. roslaunch ~/.autoware/my_launch/my_motion_planning.launch
