#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
import math

def publish_joint_states():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_test_publisher')
    rate = rospy.Rate(100)  # 10 Hz
    angle1 = 0.0
    angle2 = 0.0
    angle3 = 0.0

    while not rospy.is_shutdown():
        angle1 += 0.01
        angle2 += 0.01
        angle3 += 0.01
        js = JointState()
        js.header.stamp = rospy.Time.now()
        js.name = ['joint1', 'joint2', 'joint3']
        js.position = [1.0, 0.5, -0.2]
        #js.position = [math.sin(angle1), math.sin(angle2), math.sin(angle3)]
        # js.velocity = [0.1, 0.1, 0.1]
        pub.publish(js)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_states()
    except rospy.ROSInterruptException:
        pass
