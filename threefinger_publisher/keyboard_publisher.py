import threading
import rclpy
import os

from example_interfaces.msg import Float64MultiArray


def handle_keyboard(publisher):
    STEP_INCREASE = 1000
    motor1 = 0
    motor2 = 0
    motor3 = 0
    while True:
        print('\n- Welcome to three finger tool calibration menu -')
        print('\n- Select one of the options below. You can then use z or x  keys to move the fingers to find the limits -')
        print('   1. Motor number 1')
        print('   2. Motor number 2')
        print('   3. Motor number 3')
        print('   9. Back to menu')
        print('   0. Exit')

        menu = input('Input the menu: ')
        if menu in ['1', '2', '3']:
            key = 0
            while key not in ['0', '9'] :
                key = input(f'Press z:+{STEP_INCREASE}, x:-{STEP_INCREASE}, 9 for menu: ')
                if key == 'z':   # up arrow
                    step = STEP_INCREASE
                elif key == 'x': # down arrow
                    step = - STEP_INCREASE
                elif key == '9':
                    break
                
                if menu == '1':
                    motor1 = motor1 + step
                elif menu == '2':
                    motor2 = motor2 + step
                elif menu == '3':
                    motor3 = motor3 + step

                msg = Float64MultiArray(data = [motor1, motor2, motor3])
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