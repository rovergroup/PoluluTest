#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from dual_g2_hpmd_rpi import motors, MAX_SPEED

def subscriber():

	sub = rospy.Subscriber('command_drive_pwr', Float32, callback_function)
	rospy.spin()

def callback_function(message):

	cmd_pwr = int(message.data * float(MAX_SPEED))
	rospy.loginfo("Command Recieved: %s"%cmd_pwr)
	

	motors.enable()
	motors.setSpeeds(cmd_pwr, cmd_pwr)
	
	#motors.setSpeeds(0,0)
	#motors.disable()

if __name__ == "__main__":
	rospy.init_node("simple_subscriber")
	subscriber()

