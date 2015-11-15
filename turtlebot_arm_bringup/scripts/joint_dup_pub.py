#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState


curPos = 0.0
curVel = 0.0

def recvJointStates(msg):
    global curPos, curVel
    for i, name in enumerate(msg.name):
        if name == "gripper_joint":
            curPos = -msg.position[i]
            curVel = -msg.velocity[i]


rospy.init_node("fake_joint_dup_pub")
p = rospy.Publisher('joint_states', JointState, queue_size=5)
sub = rospy.Subscriber('joint_states', JointState, recvJointStates)

msg = JointState()
msg.name = ["gripper2_joint"]

while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()
    msg.position = [curPos for name in msg.name]
    msg.velocity = [curVel for name in msg.name]
    p.publish(msg)
    rospy.sleep(0.05)


