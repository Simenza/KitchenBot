#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Vector3
from tf2_ros import TransformBroadcaster

class OdomToTF(Node):
    def __init__(self):
        super().__init__('odom_to_tf')
        self.broadcaster = TransformBroadcaster(self)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)

    def odom_callback(self, msg):
        # Log dei dati di posizione e orientamento
        self.get_logger().info(f"Position: x={msg.pose.pose.position.x}, y={msg.pose.pose.position.y}, z={msg.pose.pose.position.z}")
        self.get_logger().info(f"Orientation: x={msg.pose.pose.orientation.x}, y={msg.pose.pose.orientation.y}, z={msg.pose.pose.orientation.z}, w={msg.pose.pose.orientation.w}")

        # Creazione del messaggio di trasformazione
        t = TransformStamped()
        t.header.stamp = msg.header.stamp
        t.header.frame_id = msg.header.frame_id  # ad esempio: differential_drive_robot/odom
        t.child_frame_id = 'body_link'    # ad esempio: differential_drive_robot/body_link
        
        # Conversione corretta della posizione in Vector3
        t.transform.translation = Vector3(x=msg.pose.pose.position.x, 
                                          y=msg.pose.pose.position.y, 
                                          z=msg.pose.pose.position.z)
        
        # Conversione corretta dell'orientamento in Quaternion
        t.transform.rotation = msg.pose.pose.orientation

        # Invio della trasformazione
        self.broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = OdomToTF()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
