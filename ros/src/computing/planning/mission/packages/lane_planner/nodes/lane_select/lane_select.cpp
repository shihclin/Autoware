/*
 *  Copyright (c) 2015, Nagoya University
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *  * Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer.
 *
 *  * Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 *  * Neither the name of Autoware nor the names of its
 *    contributors may be used to endorse or promote products derived from
 *    this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 *  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 *  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 *  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 *  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <ros/ros.h>
#include <iostream>

#include "waypoint_follower/LaneArray.h"
#include "runtime_manager/ConfigLaneSelect.h"

/*=============*/
#include <chrono>

/*===============*/
static double lane_select_time = 0.0;
static std::chrono::time_point<std::chrono::system_clock> lane_select_start, lane_select_end;
/*===============*/



static ros::Publisher g_pub;
static int g_lane_number = 0;
static waypoint_follower::LaneArray g_lane_array;

static void configCallback(const runtime_manager::ConfigLaneSelectConstPtr &config)
{
  g_lane_number = config->number;
  if ((int)g_lane_array.lanes.size() > g_lane_number)
    g_pub.publish(g_lane_array.lanes[g_lane_number]);
}

static void laneArrayCallback(const waypoint_follower::LaneArrayConstPtr &msg)
{
  g_lane_array = *msg;
  if ((int)g_lane_array.lanes.size() > g_lane_number)
  {
    /*=====*/
    lane_select_start = std::chrono::system_clock::now();
    g_pub.publish(g_lane_array.lanes[g_lane_number]);
    /*=====*/
    lane_select_end = std::chrono::system_clock::now();
    lane_select_time = std::chrono::duration_cast<std::chrono::microseconds>(lane_select_end - lane_select_start).count();
    std::cout << "Lane select time: " << lane_select_time << " us." << std::endl;
  }
  else{
  	std::cout<<"size < lane_number"<<std::endl;
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "lane_select");
  ROS_INFO("Enter Lane select");


  ros::NodeHandle nh;
  ros::Subscriber config_sub = nh.subscribe("/config/lane_select", 1, configCallback);
  ros::Subscriber sub = nh.subscribe("traffic_waypoints_array", 1, laneArrayCallback);
  g_pub = nh.advertise<waypoint_follower::lane>("base_waypoints", 10, true);

  ros::spin();
  return 0;
}
