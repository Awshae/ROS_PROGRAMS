#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class MyNode(Node):
    def __init__(self):
        super().__init__("Message_pub")
        self.publisher_text =self.create_publisher( String,"/exam_text",10)
        self.publisher_Int =self.create_publisher( Int32,"/exam_number",10)
        self.timer_ = self.create_timer(0.5,self.publish_msg)
        self.count = 0
        self.get_logger().info("messages have started")
    
    def publish_msg(self):
        text_msg=String()
        text_msg.data = "text text text"
        self.publisher_text.publish(text_msg)

        num_msg=Int32()
        num_msg.data= self.count
        self.publisher_Int.publish(num_msg)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()