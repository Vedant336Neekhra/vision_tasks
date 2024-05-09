#!/usr/bin/env python3

import rospy
import roslaunch
from std_msgs.msg import String

def launch_nodes():
    rospy.init_node('lab1_launch', anonymous=True)
    rospy.set_param('/talker_node/v', 1.5)
    rospy.set_param('/talker_node/d', 0.3)
    talker_node = roslaunch.core.Node(
        package='lab1_pkg',
        node_type='talker.py',
        name='talker_node',
        output='screen'
    )

    relay_node = roslaunch.core.Node(
        package='lab1_pkg',
        node_type='relay.py',
        name='relay_node',
        output='screen'
    )
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    launch.launch(talker_node)
    launch.launch(relay_node)

if __name__ == '__main__':
    try:
        launch_nodes()
    except rospy.ROSInterruptException:
        pass

