"""This module uses the new Create API to control the Create.
To use it you must fist call 'connect' and when done call 'disconnect'."""


from wallaby import *
from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES


right_encoder_initial = None
left_encoder_initial = None
robot = None
turn_diameter = 9.5
port = '/dev/ttyUSB0'
create_initialized = False


def connect():
    """Connect to the create - must be called before anything else is used."""
    global robot
    global create_initialized
    create_initialized = True
    try:
        robot = Create2(port)
    except Exception:
        print('The Create is either not connected or is powered off.')
        exit(1)
    robot.oi_mode = MODES.SAFE
    _set_initial_counts()


def drive(left, right, time):
    """Drive normally"""
    left *= 5
    right *= 5
    _verify()  # Check if create is connected
    robot.drive_direct(left, right)
    msleep(time)
    robot.drive_direct(0, 0)


def drive_distance(distance, base_speed, diff=25, refresh_rate=0):
    """Drive straight a distance"""
    _verify()  # Check if create is connected
    # save initial encoder vals (they'll roll over, so we need to adjust for this eventually
    _set_initial_counts()
    base_speed *= 5
    if base_speed > 475:
        base_speed = 475
    # master is left wheel
    left_speed = base_speed
    while _convert_to_inches(_left_encoder()) < distance - 0.75:
        r_encoder = _right_encoder()
        l_encoder = _left_encoder()
        if r_encoder > l_encoder:
            left_speed = base_speed - diff
        if l_encoder > r_encoder:
            left_speed = base_speed + diff
        robot.drive_direct(int(left_speed), int(base_speed))
        msleep(refresh_rate)
    robot.drive_direct(0, 0)


def rotate(degrees, speed):
    """Rotate using both wheels"""
    _verify()  # Check if create is connected
    _set_initial_counts()
    if speed < 0:
        speed *= -1
    if degrees < 0:
        speed *= -1
    degrees = abs(degrees) - 5
    if degrees < 0:
        degrees = 0
    circ_percent = degrees / 360.0
    circ = 3.1415 * turn_diameter
    dist = circ_percent * circ
    robot.drive_direct(speed, -speed)
    while _convert_to_inches((abs(_left_encoder()) + abs(_right_encoder())) / 2.0) < dist:
        pass
    robot.drive_direct(0, 0)


def pivot_on_left(degrees, speed):
    """Pivot keeping the left wheel still"""
    _verify()  # Check if create is connected
    _set_initial_counts()
    if speed < 0:
        speed *= -1
    if degrees < 0:
        speed *= -1
    degrees = abs(degrees) - 5
    if degrees < 0:
        degrees = 0
    circ_percent = degrees / 360.0
    circ = 3.1415 * turn_diameter * 2
    dist = circ_percent * circ
    robot.drive_direct(speed, 0)
    while _convert_to_inches(abs(_right_encoder())) < dist:
        pass
    robot.drive_direct(0, 0)


def pivot_on_right(degrees, speed):
    """Pivot keeping the right wheel still"""
    _verify()  # Check if create is connected
    _set_initial_counts()
    if speed < 0:
        speed *= -1
    if degrees < 0:
        speed *= -1
    degrees = abs(degrees) - 5
    if degrees < 0:
        degrees = 0
    circ_percent = degrees / 360.0
    circ = 3.1415 * turn_diameter * 2
    dist = circ_percent * circ
    robot.drive_direct(0, speed)
    while _convert_to_inches(abs(_left_encoder())) < dist:
        pass
    robot.drive_direct(0, 0)


def disconnect():
    """Disconnect from the create"""
    _verify()  # Check if create is connected
    robot.stop()


def _set_initial_counts():
    """Set the initial encoder counts."""
    _verify()  # Check if create is connected
    global right_encoder_initial
    global left_encoder_initial
    right_encoder_initial = robot.right_encoder_counts
    left_encoder_initial = robot.left_encoder_counts


def _left_encoder():
    """Returns the left encoder's ticks. Make sure to have called '_set_initial_counts' before use."""
    _verify()  # Check if create is connected
    return (int(robot.left_encoder_counts) - int(left_encoder_initial))


def _right_encoder():
    """Returns the right encoder's ticks. Make sure to have called '_set_initial_counts' before use."""
    _verify()  # Check if create is connected
    return (int(robot.right_encoder_counts) - int(right_encoder_initial))


def _convert_to_inches(ticks):
    """Convert encoder ticks to inches"""
    dist = ((3.1415 * 72.0 / 508.8) * ticks) / 25.4
    return dist


def _verify():
    """Checks if the create is connected. Exits if not connected."""
    if not create_initialized:
        print('Please call \'connect\' at the start of your program!')
        exit(1)
