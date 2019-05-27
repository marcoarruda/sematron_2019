#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

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
    # print regions

def take_decision():
    msg = Twist()

    if regions['front'] < 0.4:
        # turn left or right
        msg.linear.x = 0
        if regions['left'] > regions['right']:
            print 'turn left'
            msg.angular.z = 0.4
        else:
            print 'turn right'
            msg.angular.z = -0.4
    else:
        print 'go straight ahead'
        # go straight ahead
        msg.linear.x = 0.4
        msg.angular.z = 0

    return msg

def main():
    # initialize node
    rospy.init_node('obstacle_avoidance')

    # declare publisher and subscriber
    rospy.Subscriber("/scan", LaserScan, callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # define loop rate
    rate = rospy.Rate(20)

    # start loop
    while not rospy.is_shutdown():
        msg = take_decision()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    main()