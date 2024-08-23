#!/usr/bin/env python3

import rospy
from bonus_pkg.msg import node1message  # Custom message for Node 1
from bonus_pkg.msg import node2message   # Custom message for Node 2

def callback(msg):
    rospy.loginfo(f"Node1 received: {msg.message2}")

def node1():
    rospy.init_node('node1', anonymous=True)

    pub = rospy.Publisher('chat', node1message, queue_size=10)
    rospy.Subscriber('chat', node2message, callback)

    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        msg = node1message()
        msg.message1 = input("Node 1 getting input")
        rospy.loginfo("Node1 sending: " + msg.message1)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
