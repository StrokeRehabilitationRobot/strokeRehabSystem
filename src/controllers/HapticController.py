#!/usr/bin/env python

import rospy
from strokeRehabSystem.msg import *
from geometry_msgs.msg import Pose,Point, WrenchStamped
import math
class HapticController():

    def __init__(self, k_obs, k_goal, d_obs, d_goal, goal_angle=math.pi/3.0 ):
        """
        """
        #rospy.init_node("haptics",anonymous=True)
        self.pub = rospy.Publisher("motors_server", WrenchStamped, queue_size=1)
        self.k_obs  = -k_obs
        self.k_goal = k_goal
        self.d_obs  = d_obs
        self.d_goal = d_goal
        self.goal_angle = goal_angle

    def make_force(self,player, obstacles=[],goals=[]):

        forces = WrenchStamped()
        forces.header.frame_id = "master"

        f_y = 0
        f_x = 0

        for goal_num, g in enumerate(goals):
            #print "g",g
            d = math.sqrt( (g.x - player.x)**2 + (g.y - player.y)**2  )
            theta_gp = math.atan2( (g.y - player.y),(g.x - player.x) )
            if len(goals) == 1:
                F = self.k_goal * ( max(self.d_goal - d,0))
                f_y += round(F*math.sin(theta_gp),2)
                f_x += round(F*math.cos(theta_gp),2)
            else:
                if goal_num == 0:
                    continue
                theta_gg = math.atan2( (goals[goal_num].y - goals[goal_num - 1].y),(goals[goal_num].x - goals[goal_num - 1].x) )
                if abs(theta_gg  - theta_gp) <= self.goal_angle:
                    F = self.k_goal * ( max(self.d_goal - d,0))
                    f_y += round(F*math.sin(theta_gp),2)
                    f_x += round(F*math.cos(theta_gp),2)


        for obs in obstacles:
            d = math.sqrt( (obs.x - player.x)**2 + (obs.y - player.y)**2  )
            theta = math.atan2( (obs.y - player.y),(obs.x - player.x) )
            F = self.k_obs * ( max(self.d_obs - d,0))
            f_y += round(F*math.sin(theta),2)
            f_x += round(F*math.cos(theta),2)

        [forces.wrench.force.x, forces.wrench.force.y, forces.wrench.force.z] = [ round(f_x,1), 0, -round(f_y, 1) ]
        self.pub.publish(forces)
