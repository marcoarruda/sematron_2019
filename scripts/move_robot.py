#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def main():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move_robot')
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 0.4
        msg.angular.z = 0.4
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass