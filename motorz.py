from wallaby import clear_motor_position_counter
from wallaby import freeze
from wallaby import get_motor_position_counter
from wallaby import msleep
from wallaby import seconds
from wallaby import analog
from wallaby import motor_power as motor
from wallaby import motor_power
from wallaby import digital
from constants import *

def rotate_spinner(rotations, speed):
    full_rotation = 1400.0
    start = get_motor_position_counter(clawMotor)
    motor_power(clawMotor, speed)

    tries_remaining = 3
    previous = 0
    counter = 0

    while abs(get_motor_position_counter(clawMotor) - start) < abs(full_rotation * rotations) and tries_remaining > 0:
        if counter >= 10:
            counter = 0
            if tries_remaining > 0:
                motor_power(clawMotor, int(-speed))
                msleep(300)
                motor_power(clawMotor, speed)
            tries_remaining -= 1
        elif abs(get_motor_position_counter(clawMotor)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(clawMotor))
        msleep(10)
    print "rotated {} out of {}".format(get_motor_position_counter(clawMotor) - start, abs(full_rotation * rotations))
    freeze(clawMotor)


def rotate_until_stalled(speed):
    counter = 0
    motor_power(clawMotor, speed)
    previous = abs(get_motor_position_counter(clawMotor))
    while counter < 10:
        if abs(get_motor_position_counter(clawMotor)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(clawMotor))
        msleep(10)
    freeze(clawMotor)


def wait_for_someone_to_rotate():
    print("please spin me back")
    clear_motor_position_counter(clawMotor)
    while abs(get_motor_position_counter(clawMotor)) < 350:
        pass
    print("good job")


def claw_to_position(position, power):
    power = abs(power)
    while get_motor_position_counter(clawMotor) < position:
        motor_power(clawMotor, power)
        print('+ {}/{}'.format(get_motor_position_counter(clawMotor), position))
    while get_motor_position_counter(clawMotor) > position:
        print('- {}/{}'.format(get_motor_position_counter(clawMotor), position))
        motor_power(clawMotor, -power)
    freeze(clawMotor)


def set_claw_open():
    clear_motor_position_counter(clawMotor)


def claw_move(power):
    motor_power(clawMotor, power)


def test():
    rotate_until_stalled(20)
    rotate_until_stalled(-20)
    set_claw_open()
    claw_to_position(600, 20)
    exit(0)
