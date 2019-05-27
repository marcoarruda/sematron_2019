#!/usr/bin/env python

import rospy
def my_1st_node():

    rospy.init_node('my_1st_node')

    rospy.spin()


if __name__ == '__main__':
    try:
        my_1st_node()
    except rospy.ROSInterruptException:
        pass