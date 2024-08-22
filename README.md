# AUV_TASK_2
This repository contains ROS1 packages developed for various tasks related to a basic chat application and node communication.

1. task1_package
  Creates four nodes (two publishers and two subscribers) that communicate via two topics (t1 and t2).
    Files:
      publisher1.py: First publisher node, sends messages to t1.
      publisher2.py: First subscriber node, receives messages from t1.
      subscriber1.py: Second publisher node, sends messages to t2.
      subscriber2.py: Second subscriber node, receives messages from t2.
2. task2_package
  Implements a single node that acts as both a publisher and a subscriber, allowing multiple instances to communicate on the same topic.
  Files:
      chat_node.py: Node that sends and receives messages on the chat topic.
3. task_bonus_package
  Simulates a basic chat bot between two nodes, ensuring they don’t receive their own messages.(which is executed at call back function).
  Files:
    chat_node1.py: First chat node.
    chat_node2.py: Second chat node.
