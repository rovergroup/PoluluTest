#!/usr/bin/python

import rospy
from std_msgs.msg import Float32

def publisher():
	pub = rospy.Publisher('command_drive_pwr', Float32, queue_size=10)

	rate = rospy.Rate(1)

	msg_to_publish = Float32()

	counter = 0.0
	
	directionUp = True

	while not rospy.is_shutdown():
		msg_to_publish = counter
		if ((counter + 0.05) >= 1):
			directionUp = False
		elif ((counter - 0.05) <= 0):
			directionUp = True
		
		if (directionUp):
			counter += 0.05
		else:
			counter -= 0.05	
		pub.publish(msg_to_publish)

		rate.sleep()

if __name__ == "__main__":
	rospy.init_node("simple_publisher")
	publisher()
