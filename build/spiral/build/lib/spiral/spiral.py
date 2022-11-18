# Write the spiral control node here
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('spiral')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5 # start value timer
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def timer_callback(self):
        self.i += 1
        vel = Twist()
        radius = 600
        vel.linear.x = float(25)
        vel.angular.z = float(radius/self.i)
        msg = vel
        self.publisher_.publish(vel)
        
        


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()