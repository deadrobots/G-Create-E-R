
from wallaby import *
from math import pi
from utilities import *
import constants as c
import createPlusPlus as cpp


def drive_timed(left, right, time): #DRS forward is opposite of create forward
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def spin_cw(power, time):
    create_drive_direct(power, -power)
    msleep(time)
    create_drive_direct(0, 0)


def spin_ccw(power, time):
    create_drive_direct(-power, power)
    msleep(time)
    create_drive_direct(0, 0)


def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)

def rotateTillBlack(power):
    if power > 0:
        create_drive_direct(-power, power)
    else:
        create_drive_direct(power, -power)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()

def drive_forever(left, right):
    create_drive_direct(-right, -left)


def stop():
    create_stop()


INCH_TO_MIL = 25.4

def drive_distance2(distance, speed):
    if distance < 0:
        speed = -speed
    dist_mil = INCH_TO_MIL * distance
    time = (int)((dist_mil / speed) * 1000)
    drive_timed(speed, speed, time)


def rotate_degrees(degrees, speed):
    if degrees < 0:
        speed = -speed
        degrees = abs(degrees)
    degrees = degrees * 1.13
    set_create_total_angle(0)
    drive_forever(-speed, speed)
    while abs(get_create_total_angle()) < degrees:
        pass
    stop()

def black_left_or_right():
    return cpp.get_black_left() or cpp.get_black_right()

def driveTilBlackLCliffAndSquareUp(speed):
    cpp.drive_conditional(black_left_or_right, speed, False)
    while not cpp.get_black_left() or not cpp.get_black_right():
        if cpp.get_black_left():
            cpp.drive(0, speed)
        if cpp.get_black_right():
            cpp.drive(speed, 0)


def driveTilFrontTophatBlack(lspeed, rspeed):
    lspeed = -lspeed
    rspeed = -rspeed
    create_drive_direct(rspeed, lspeed)
    while (analog(c.FRONT_TOPHAT) < 2000):
        pass
    create_stop()

def timedLineFollowLeftFront(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if cpp.get_black_left():
            cpp.drive(speed/2, speed)
        else:
            cpp.drive(speed, speed/2)
    cpp.drive(0, 0)

def timedLineFollowFrontTophat(time):
    sec = seconds()
    while(seconds() - sec<time):
        if analog(c.FRONT_TOPHAT) < 1500:
            create_drive_direct(-100, -50)
        else:
            create_drive_direct(-50, -100)
    create_stop()

def timedLineFollowRightFront(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_create_rfcliff_amt() < 2000:
            create_drive_direct(speed, (int)(speed/1.8))
        else:
            create_drive_direct((int)(speed/1.8), speed)
        msleep(10)
    create_stop()

def lineFollowLeftFrontTilLeftBlack(speed):
    while get_create_lcliff_amt() > 2000:
        if get_create_lfcliff_amt() < 2000:
            create_drive_direct(speed, speed/2)
        else:
            create_drive_direct(speed/2, speed)
    create_stop()

def lineFollowLeftFrontTilRightFrontBlack(speed):
    while get_create_rfcliff_amt() > 2000:
        if get_create_lfcliff_amt() < 2000:
            create_drive_direct(speed, speed/2)
        else:
            create_drive_direct(speed/2, speed)
    create_stop()

def lineFollowRightFrontTilLeftFrontBlack(speed):
    while get_create_lfcliff_amt() > 2000:
        if get_create_rfcliff_amt() < 2000:
            create_drive_direct(speed/2, speed)
        else:
            create_drive_direct(speed, speed/2)
    create_stop()

def lineFollowRightFrontTilRightBlack():
    while get_create_rcliff_amt() > 2000:
        if get_create_rfcliff_amt() < 2000:
            create_drive_direct(200, 100)
        else:
            create_drive_direct(100, 200)
    create_stop()

def turnTilRightFrontBlack(left, right):
    create_drive_direct(left, right)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()

#unused functions to be deleted

# def drive_accel(speed, time):   #cut
#     for sub_speed in range(0, speed+1, 100):
#         create_drive_direct(-sub_speed, -sub_speed)
#         msleep(100)
#     msleep(time)
#     create_drive_direct(0, 0)
#
# def timedLineFollow(time):  #cut
#     sec = seconds()
#     while(seconds() - sec<time):
#         if get_create_lfcliff_amt() < 2000:
#             create_drive_direct(200, 150)
#         else:
#             create_drive_direct(150, 200)
#     create_stop()
#
# def lineFollowTilCrossBlack():  #cut
#     while(get_create_lcliff_amt() > 2000):
#         if get_create_lfcliff_amt() < 2000:
#             create_drive_direct(200, 150)
#         else:
#             create_drive_direct(150, 200)
#     while (get_create_lcliff_amt() < 2000):
#         if get_create_lfcliff_amt() < 2000:
#             create_drive_direct(200, 150)
#         else:
#             create_drive_direct(150, 200)
#     create_stop()
#
# def split_drive(left, right, time, increments, turnTime):   #cut
#     power = -100
#     if turnTime < 0:
#         turnTime = abs(turnTime)
#         power = abs(power)
#     if turnTime == 0:
#         drive_timed(left, right, time)
#     else:
#         for _ in range(0, increments):
#             drive_timed(left, right, int(time / increments))
#             rotate(power, turnTime)
#
#
# def split_drive_condition(left, right, min, time, turnTime, condition, state=True): #cut
#     start = seconds() + time
#     create_drive_direct(-left, -right)
#     msleep(min)
#     while condition() is state:
#         current = seconds()
#         if current > start:
#             print turnTime
#             start = current + time
#             rotate(-100, turnTime)
#             create_drive_direct(left, right)
#             msleep(min)
#     create_drive_direct(0, 0)
#
#
# def drive_conditional(left, right, testFunction, state=True):   #cut
#     create_drive_direct(-right, -left)
#     while testFunction() is state:
#         pass
#     stop()
#
# def driveTilBlackLCliff(speed):
#     create_drive_direct(-speed, -speed)
#     while (get_create_lcliff_amt() > 2000):
#         pass
#     create_stop()
#
# def driveTilBlackLFCliff(speed):
#     create_drive_direct(-speed, -speed)
#     while (get_create_lfcliff_amt() > 2000):
#         pass
#     create_stop()
#
# def driveTilWhiteLCliff(speed):
#     create_drive_direct(-speed, -speed)
#     while (get_create_lcliff_amt() < 2000):
#         pass
#     create_stop()
#
# def driveTilWhiteLFCliff(speed):
#     create_drive_direct(-speed, -speed)
#     while (get_create_lfcliff_amt() < 2000):
#         pass
#     create_stop()
#
# def driveTilBlackRCliff(speed):
#     create_drive_direct(speed, speed)
#     while (get_create_rcliff_amt() > 2000):
#         pass
#     create_stop()
#
# def turnTilBlackLCliff(left, right):
#     create_drive_direct(left, right)
#     while (get_create_lcliff_amt() > 2000):
#         pass
#     create_stop()
#
# def turnTilBlackRCliff(left, right):
#     create_drive_direct(left, right)
#     while (get_create_rcliff_amt() > 2000):
#         pass
#     create_stop()
#
#
# def driveAcrossBlack(speed):
#     create_drive_direct(speed, speed)
#     while (get_create_lcliff_amt() > 2000):
#         pass
#     while (get_create_lcliff_amt() < 2000):
#         pass
#     msleep(100)
#     create_stop()
#
# def turnAcrossBlack(left, right):
#     create_drive_direct(left, right)
#     while (get_create_lfcliff_amt() > 2000):
#         pass
#     while (get_create_lfcliff_amt() < 2000):
#         pass
#     msleep(200)
#     create_stop()
#
# def driveUntilBlue(speed):
#     create_drive_direct(speed, speed)
#     while (get_create_rfcliff_amt() > 2000):
#         pass
#     create_stop()
#
# def timedLineFollowLeft(time):
#     sec = seconds()
#     while(seconds() - sec<time):
#         if get_create_lcliff_amt() < 2000:
#             create_drive_direct(100, 50)
#         else:
#             create_drive_direct(50, 100)
#     create_stop()
#
#
# def timedLineFollowRightFrontBlocks(speed, time):
#     sec = seconds()
#     while(seconds() - sec<time):
#         if get_create_rfcliff_amt() < 2000:
#             create_drive_direct((int)(speed / 1.8), speed)
#         else:
#             create_drive_direct(speed, (int)(speed / 1.8))
#     create_stop()
#
# def lineFollowLeftFrontTilWhite():
#     while (get_create_lcliff_amt() < 2000):
#         if get_create_lfcliff_amt() < 2000:
#             create_drive_direct(100, 50)
#         else:
#             create_drive_direct(50, 100)
#     create_stop()
#
#
#
# def timedLineFollowRight(time):
#     # This is a line follow
#     # Needs to be less severe because final angle
#     # Center value? (Gray value in between White and Black)
#     sec = seconds()
#     while(seconds() - sec<time):
#         if get_create_rcliff_amt() < 2000:
#             create_drive_direct(50, 100)
#         else:
#             create_drive_direct(100, 80)
#     create_stop()
#
# def driveTillRightBump (lspeed, rspeed ):
#     create_drive_direct(-lspeed, -rspeed)
#     while get_create_rbump() == 0:
#        pass
#     create_stop()
#     print("rbump press")
#
# def driveTillBump(lspeed, rspeed):
#    # create_drive_direct(-lspeed, -rspeed)
#     while get_create_rbump() == 0 and  get_create_lbump() == 0:
#         pass
#     create_stop()
#     print("bumped")
#
#
# def driveTilWhiteLCliffAndSquareUp(lspeed, rspeed):
#     lspeed = -lspeed
#     rspeed = -rspeed
#     create_drive_direct(rspeed, lspeed)
#     while (lspeed or rspeed):
#         if get_create_lcliff_amt() > 2000:
#             lspeed = 0
#             create_drive_direct(lspeed, rspeed)
#         if get_create_rcliff_amt() > 2000:
#             rspeed = 0
#             create_drive_direct(lspeed, rspeed)

