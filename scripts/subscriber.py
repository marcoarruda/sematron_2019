#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    print 'Received (%s)' % data.data

def subscriber():

    rospy.init_node('subscriber')

    rospy.Subscriber("a_topic", String, callback)

    rospy.spin()

if __name__ == '__main__':
    subscriber()