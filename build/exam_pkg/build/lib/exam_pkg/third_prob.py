#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("exam_publisher2")
        self.publisher_ =self.create_publisher( String,"/exam_status",10)
        self.timer_ = self.create_timer(0.5,self.publish_exam)
        self.get_logger().info("Exam publisher has started")
    
    def publish_exam(self):
        msg=String()
        msg.data = "Lab Exam in progress"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()