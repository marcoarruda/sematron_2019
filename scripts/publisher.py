#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('a_topic', String)
    rospy.init_node('publisher')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "publishing at [%s]" % rospy.get_time()
        print hello_str
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass