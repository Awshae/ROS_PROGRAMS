#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("exam_subscriber")
        self.subscription_ =self.create_subscription( String,"/exam_status",self.listener_callback,10)
        self.get_logger().info("Exam subscription has started")
    
    def listener_callback(self, msg):
        self.get_logger().info(f'recieved: "{msg.data}"')
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()