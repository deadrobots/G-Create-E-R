
from wallaby import *
from math import pi
from utilities import *
import constants as c

cpp = None

def init_movement(icpp):
    global cpp
    cpp = icpp

#   sensor assisted driving
#   linefollows and whatnot

def lineFollowLeftFrontTilRightFrontBlack(speed):
    while cpp.get_black_front_right():
        if not cpp.get_black_front_left():
            cpp.drive(speed, speed / 2)
        else:
            cpp.drive(speed / 2, speed)
    cpp.drive(0, 0)


def lineFollowRightFrontTilLeftFrontBlack(speed):
    while cpp.get_black_front_left():
        if not cpp.get_black_front_right():
            cpp.drive(speed / 2, speed)
        else:
            cpp.drive(speed, speed / 2)
    cpp.drive(0, 0)

#   sensor conditional movements
#   drive unguided until condition

def driveTilFrontTophatBlack(lspeed, rspeed):
    cpp.drive(rspeed, lspeed)
    while (not black_tophat()):
        pass
    cpp.drive(0,0)

def driveTilBlackLCliffAndSquareUp(lspeed, rspeed):
    cpp.drive(rspeed, lspeed)
    while (lspeed or rspeed):
        if not cpp.get_black_left():
            lspeed = 0
            cpp.drive(lspeed, rspeed)
        if not cpp.get_black_right():
            rspeed = 0
            cpp.drive(lspeed, rspeed)
    cpp.drive(0, 0)

def turnTilRightFrontBlack(left, right):
    cpp.drive(left, right)
    while cpp.get_black_front_right():
        pass
    cpp.drive(0,0)

def driveTilBlackLRCliffAndSquareUp(lspeed, rspeed):
    cpp.drive(lspeed, rspeed)
    while not cpp.get_black_left() and not cpp.get_black_right():
        pass
    cpp.drive(0,0)

def rotateTillBlack(power):
    if power > 0:
        cpp.drive(-power, power)
    else:
        cpp.drive(power, -power)
    while (cpp.get_black_front_right):
        pass
    create_stop()
    cpp.drive(0, 0)

#   sacred grayson code
#   use as reference for functions

def squareUpOnBlack(speed):
    if speed > 0:
        cpp.drive_conditional(black_left_or_right, speed, False)
        while not cpp.get_black_left() or not cpp.get_black_right():
            if cpp.get_black_left():
                cpp.drive(-speed, 0)
                print ("left")
            elif cpp.get_black_right():
                cpp.drive(0, -speed)
                print ("right")
            else:
                print ("None")
    else:
        cpp.drive_conditional(black_left_or_right, speed, False)
        while not cpp.get_black_left() or not cpp.get_black_right():
            if cpp.get_black_left():
                cpp.drive(-speed, 0)
                print ("left")
            elif cpp.get_black_right():
                cpp.drive(0, -speed)
                print ("right")
            else:
                print ("None")
    print ("done!")
    cpp.drive(0, 0)

def black_left_or_right():
    return cpp.get_black_left() or cpp.get_black_right()

def black_tophat():
    return analog(c.FRONT_TOPHAT) > 2000

#   old API functions
#   still used in later parts of routine
#   CHANGE TO createPlusPlus IN ACTIONS

'''

def spin_cw(power, time):
    cpp.drive(power, -power)
    msleep(time)
    cpp.drive(0, 0)

def spin_ccw(power, time):
    cpp.drive(-power, power)
    msleep(time)
    cpp.drive(0, 0)

def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)'''

#   new code cemetary
#   unused functions to be deleted

'''
def timedLineFollowFrontTophatForward(time):  # not used
    sec = seconds()
    while (seconds() - sec < time):
        if black_tophat():
            cpp.drive(25, 50)
        else:
            cpp.drive(50, 25)
    cpp.drive(0, 0)


def driveTillBump(lspeed, rspeed):  # not used
    cpp.drive(rspeed, lspeed)
    while not cpp.left_bump() and not cpp.right_bump():
        pass
    cpp.drive(0, 0)


def driveTilWhiteLRCliffAndSquareUp(lspeed, rspeed):  # not used
    # print(cpp.TEMP_GET_ROBOT().cliff_right_signal)
    cpp.drive(lspeed, rspeed)
    while cpp.get_black_left():
        cpp.drive(0, abs(rspeed) / rspeed * 5)
        print('black on right')
    while cpp.get_black_right():
        cpp.drive(abs(lspeed) / lspeed * 5, 0)
        print('black on left')
    cpp.drive(0, 0)

def driveTilBlackFrontLRCliffAndSquareUp(lspeed, rspeed):  # not used
    cpp.drive(lspeed, rspeed)
    while not cpp.get_black_front_left() and not cpp.get_black_front_right():
        pass
    cpp.drive(0, 0)

def lineFollowRightFrontTilRightBlack(speed):   #not used
    while not cpp.get_black_right():
        if not cpp.get_black_front_right():
            cpp.drive(speed/2, speed)
        else:
            cpp.drive(speed, speed/2)
    cpp.drive(0,0)

def timedLineFollowLeftFront(speed, time):  #not used
    sec = seconds()
    while(seconds() - sec<time):
        if not cpp.get_black_front_left():
            cpp.drive(speed, speed/2)
        else:
            cpp.drive(speed/2, speed)
    cpp.drive(0,0)

def timedLineFollowRightFront(speed, time): #not used
    sec = seconds()
    while(seconds() - sec<time):
        if not cpp.get_black_front_right():
            cpp.drive(speed, (int)(speed/1.8))
        else:
            cpp.drive((int)(speed/1.8), speed)
        msleep(10)
    cpp.drive(0,0)

def lineFollowLeftFrontTilLeftBlack(speed): #not used
    while cpp.get_black_left():
        if not cpp.get_black_front_left():
            cpp.drive(speed, speed/2)
        else:
            cpp.drive(speed/2, speed)
    cpp.drive(0,0)'''