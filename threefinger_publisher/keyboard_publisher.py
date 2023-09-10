import threading
import rclpy
import os

from example_interfaces.msg import Float64MultiArray

CLOSE_POSITION = [ 50000, -100000, 1000]
OPEN_POSITION = [ -20000, 0, 0]

def handle_keyboard(publisher):
    STEP_INCREASE = 1000
    STEP_INCREASE_LARGE = 10000
    motor1 = 0
    motor2 = 0
    motor3 = 0
    while True:
        print('\n- Welcome to three finger tool calibration menu -')
        print('\n- Select one of the options below. You can find the limits for individual motors and then saved the limits -')
        print('   1. Motor number 1')
        print('   2. Motor number 2')
        print('   3. Motor number 3')
        print('   4. Move all motors to ZERO (0,0,0)')
        print('   5. Move all motors to OPEN (Based on saved values)')
        print('   6. Move all motors to CLOSE (Based on saved values)')
        print('   9. Back to menu')
        print('   0. Exit')

        menu = input('Input the menu: ')
        if menu in ['1', '2', '3']:
            key = 0
            while key not in ['m'] :
                key = input(f'Enter a value for motor {menu}, m for menu: ')

                if key == 'm':
                    break
                else:
                    new_motor_value = int(key)
                    if menu == '1':
                        motor1 = new_motor_value
                    elif menu == '2':
                        motor2 = new_motor_value
                    elif menu == '3':
                        motor3 = new_motor_value

                msg = Float64MultiArray(data = [motor1, motor2, motor3])
                publisher.publish(msg)
                print(" \n>>> command is published : {0}".format(msg.data))
        
        elif menu == '4':
            msg = Float64MultiArray(data = [0,0,0])
            publisher.publish(msg)
            print(" \n>>> command is published : {0}".format(msg.data))
        
        elif menu == '5':
            msg = Float64MultiArray(data = OPEN_POSITION)
            publisher.publish(msg)
            print(" \n>>> command is published : {0}".format(msg.data))
        
        elif menu == '6':
            msg = Float64MultiArray(data = CLOSE_POSITION)
            publisher.publish(msg)
            print(" \n>>> command is published : {0}".format(msg.data))

        elif menu == '0':
            rclpy.shutdown()
            os._exit(1)


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node("keyboard_publisher")
    publisher = node.create_publisher(Float64MultiArray, "/joint_angles", 10)

    th = threading.Thread(target=handle_keyboard, args=(publisher,))
    th.start()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()