#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class miNode(Node):
    def __init__(self):
        super().__init__("tesing_publisher")
        self.publisher = self.create_publisher(String,"/ooops",10)
        self.timer = self.create_timer(0.5,self.publish_exam)
        self.get_logger().info("WORK")

    def publish_exam(self):
        msg = String()
        msg.data = "Hie jkgvnojsf"
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = miNode()
    rclpy.spin(node)
    rclpy.shutdown(node)

if __name__ == "__main__":
    main()

