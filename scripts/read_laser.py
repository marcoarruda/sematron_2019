#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

regions = {
    'front': 0,
    'left': 0,
    'back': 0,
    'right': 0
}

def callback(data):
    regions['front'] = min(min(data.ranges[0:45] + data.ranges[315:359]), 3.5)
    regions['left'] = min(min(data.ranges[45:135]), 3.5)
    regions['back'] = min(min(data.ranges[135:225]), 3.5)
    regions['right'] = min(min(data.ranges[225:315]), 3.5)
    print regions

def main():

    rospy.init_node('read_laser')

    rospy.Subscriber("/scan", LaserScan, callback)

    rospy.spin()

if __name__ == '__main__':
    main()