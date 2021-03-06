#!/usr/bin/env python 
#coding: UTF-8/*
"""
kamesan.py
 
Copyright (C) 2017  Shogo Ota
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math 
import rospy
import time

class turtle_star(object):
    def __init__(self):
        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        self.sub = rospy.Subscriber('/turtle1/pose',Pose,self.parameters)
        self.speed = Twist()
        time.sleep(1)

    def parameters(self,parameters):
        self.x=parameters.x
        self.y=parameters.y
        self.theta = parameters.theta

    def run(self):
        b=0
        count=0
        self.speed.linear.x = 8
        while not rospy.is_shutdown():
            if count == 7:
                self.speed.linear.x = 0
                self.speed.angular.z = 0
            elif self.speed.linear.x == 8:
                self.speed.linear.x=0
                self.speed.angular.z=-4
                count += 1
                if count==6:
                    self.speed.linear.x=8
                    self.speed.angular.z=0
                    count = 7
            else:
                self.speed.linear.x=0
                self.speed.angular.z=-0.05
            turget=(math.pi*4/5)-b
            if turget<0:
                turget=turget+(2*math.pi)
	    if turget>2*math.pi:
		turget=turget-(2*math.pi)
            a=self.theta+turget
            if math.fabs(a)<0.02 and self.speed.angular.z==-0.05:
                self.speed.angular.z=0
                b=self.theta
                self.speed.linear.x = 8
            self.pub.publish(self.speed)
            rospy.sleep(0.5)
        
if __name__ == '__main__':
    rospy.init_node('kamekame')
    datw = turtle_star()
    try:
        datw.run()
    except rospy.ROSInterruptException:
        pass
