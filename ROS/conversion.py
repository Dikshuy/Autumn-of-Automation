#!/usr/bin/env python

import rospy
import numpy as np
from umic.msg import quat
from umic.msg import eul	

converted_values = eul()

def conversion(msg):
	x = msq.x_q
	y = msg.y_q
	z = msg.z_q
	w = msg.w_q
	sinr_cosp = 2 * (w * x + y * z)
    	cosr_cosp = 1 - 2 * (x**2 + y**2)
    	roll1 = np.arctan2(sinr_cosp, cosr_cosp)

    	sinp = 2 * (w * y - z * x)
    	pitch1 = np.where(np.abs(sinp) >= 1,np.sign(sinp) * np.pi / 2, np.arcsin(sinp))

  	siny_cosp = 2 * (w * z + x * y)
    	cosy_cosp = 1 - 2 * (y**2 + z**2)
    	yaw1 = np.arctan2(siny_cosp, cosy_cosp)
	converted_values.roll = roll1
	converted_values.pitch = pitch1
	converted_values.yaw = yaw1
	pub.publish(converted_values)

def subs():
	rospy.init_node('my_converter', anonymous=True)
	sub = rospy.Subscriber('/quaternions', quat, conversion)
	pub = rospy.Publisher('euler', eul, queue_size = 1)
	rospy.spin()

if __name__ == "__main__":
	try:
		subs()
	except rospy.ROSInterruptException:
		pass


