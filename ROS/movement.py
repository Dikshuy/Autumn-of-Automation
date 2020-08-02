#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def writing_letter():
    rospy.init_node('move', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 2
    distance = 8.5
    angle = 90

    angular_speed = 0.8
    relative_angle = angle*2*3.14/360

    vel_msg.linear.x = abs(speed)
    vel_msg.angular.z = angular_speed
    current_distance = 0
    current_angle = 0


    while(current_distance < distance):

        t0 = rospy.Time.now().to_sec()

        while(current_distance < distance):
            	velocity_publisher.publish(vel_msg)
            	t1=rospy.Time.now().to_sec()
            	current_distance= speed*(t1-t0)
	
        while(current_angle < relative_angle):
        	vel_msg.linear.x = 0
	        velocity_publisher.publish(vel_msg)
	        t1 = rospy.Time.now().to_sec()
	        current_angle = angular_speed*(t1-t0)

        
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = 0
    vel_msg.angular.z = angular_speed
    current_angle = 0
    relative_angle = 3.14/2.1
    while current_angle<relative_angle:
    	velocity_publisher.publish(vel_msg)
    	t1 = rospy.Time.now().to_sec()
    	current_angle = angular_speed*(t1-t0)
    
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = speed
    vel_msg.angular.z = 0
    current_distance = 0
    distance2 = 2.7
    while current_distance<distance2:
    	velocity_publisher.publish(vel_msg)
    	t1 = rospy.Time.now().to_sec()
    	current_distance = speed*(t1-t0)
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0

    rospy.spin()

if __name__ == '__main__':
    try:
        writing_letter()
    except rospy.ROSInterruptException: pass