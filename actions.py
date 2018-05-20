from movement import *
from utilities import *
import constants as c
from wallaby import *
from utilities import *
import constants as c
from wallaby import *

def init():
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    create_disconnect()
    if not create_connect_once():
        print("Create not connected...")
        exit(0)
    print("Create connected...")
    create_full()
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    else:
        print("I AM YELLOW!")
        DEBUG() # Do not remove!!!
    selfTest()
    print("Press right button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    shut_down_in(119.0)
    print("Running...")
    c.START_TIME = seconds()

def selfTest():
    #tests all motors and servos
    # raise arm
    print ("Running Self Test")
    testArm()
    resetArm(30, 2000)
    # open/close claw
    enable_servo(c.servoClaw)
    moveServo(c.servoClaw, c.clawClosed, 15)
    moveServo(c.servoClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    # lower ramp
    enable_servo(c.servoIgus)
    moveServo(c.servoIgus, c.cogStart - 300, 10)
    # move the chain
    moveCog(100, 1500)# enables cog
    resetChain()
    # raise ramp
    moveServo(c.servoIgus, c.cogStartBox, 10)
    msleep(250)
    # lower the arm
    moveArm(c.armStartbox, 30)
    ao()

def driveOutOfStartBox():
    print ("driving")
    rotate_degrees(30, 70)



def turnToRing():
    #squares up on south wall then west wall
    print ("turnToRing")
    resetArm(30, 2000)
    moveServo(c.servoClaw, c.clawClosed, 35)
    drive_timed(100, 100, 2000) #squares up to west wall
    if c.IS_ORANGE_BOT:
        drive_timed(-100, -75, 1375)
        drive_timed(-180, 180, 1100)
    elif c.IS_BLUE_BOT:
        drive_timed(-100, -95, 1100)
        drive_timed(-180, 180, 1100)
    drive_timed(100, 100, 1000) #square up on south wall
    moveServo(c.servoIgus, c.cogGrab, 10)
    if c.IS_ORANGE_BOT:
        moveCog_position(3.75, 95)
    elif c.IS_BLUE_BOT:
        moveCog_position(3.5, 95)
    driveTilBlackLCliff(-100)
    if c.IS_ORANGE_BOT:
        drive_timed(-30, -60, 550)
    elif c.IS_BLUE_BOT:
        drive_timed(-30, -50, 775)


def liftRing():
    print("liftRing")
    if c.IS_ORANGE_BOT:
        moveServo(c.servoIgus, c.cogStart - 250, 5)
        moveCog_position(6, 100)
        moveServo(c.servoIgus, c.cogStart - 350, 5)
    elif c.IS_BLUE_BOT:
        moveServo(c.servoIgus, c.cogStart - 380, 5)
        moveCog_position(5.7, 100)
        moveServo(c.servoIgus, c.cogStart - 480, 5)


def raiseRing2():
    # orange
    #this allows create to raise ring in the middle of the cog railway and drive
    print("raiseRing2")
    timedLineFollowLeftFront(1.9)
    moveServo(c.servoIgus, c.cogLift, 5)
    if c.IS_ORANGE_BOT:
        moveCog_position(2.5, 100)
    else:
        moveCog_position(2.0, 100)
    timedLineFollowLeftFront(1.9)
    moveServo(c.servoIgus, c.evenMoreCogLift, 5)
    if c.IS_ORANGE_BOT:
        moveCog_position(3.8, 100)
    else: #Is blue
        moveCog_position(5, 100)
    lineFollowLeftFrontTilBlack()
    lineFollowLeftFrontTilWhite()
    moveServo(c.servoIgus, c.cogServoVeryHigh, 5)
    moveArm(c.armVeryHigh, 10)
    if c.IS_ORANGE_BOT:
        moveCog_position(1.5, 100)
    else:
        moveCog_position(1.8, 100)
    timedLineFollowLeftFront(1.8)


def dropRing():
    print("dropRing")
    moveCog_position(-5, 100)
    moveServo(c.servoIgus, c.cogRingDrop, 5)
    moveCog_position(-1, 100)
    msleep(500)
    drive_timed(-50, 50, 1200)
    if c.IS_ORANGE_BOT:
        moveServo(c.servoIgus, c.cogStart-300, 3)
    else:
        moveServo(c.servoIgus, c.cogStart - 375, 3)
    moveCog_position(-6, 100)
    moveServo(c.servoIgus, c.cogRingDrop, 5)


def turnToTram():
    # Depends on position after drop, so may need to be changed as drop method changes
    # Tram keeps getting stuck on the claw pegs and the connector - need to work on sliding it without getting stuck
    print("turnToTram")
    motor(c.cogMotor, -30)
    if c.IS_ORANGE_BOT:
        drive_timed(100, 100, 800)  #-850
        rotate_degrees(-165, 100)
    else:
        drive_timed(100, 100, 765)   #780
        rotate_degrees(-160, 100)
    moveArm(c.armTram, 10)
    resetChain()


def slideTram():
    print("slideTram")
    rotate_degrees(-75, 100) # this turn is where the arm tries to connect to the tram and starts pushing it
    msleep(500) # do not remove: allows tram to settle
    if c.IS_ORANGE_BOT:
        drive_timed(250, 100, 1200)# Used to be 1200 not 900 shorter drive
    else:
        drive_timed(200, 100, 1200)  # shorter drive
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(200, 100)
    if c.IS_ORANGE_BOT:
        drive_timed(100, 100, 1370) #100, 100, 1100
    else: #is blue
        drive_timed(100, 100, 1380)   #1370


def approachCenter():
    print("approachCenter")
    rotate_degrees(92, 100) #Used to be 90
    drive_timed(100,100,1900)
    driveTilBlackLCliffAndSquareUp(-100, -100)
    msleep(500)
    moveServo(c.servoClaw, c.clawTram, 20)
    resetArm(30, 500)
    drive_timed(-100, -100, 500)
    rotate_degrees(-90, 100)
    driveTilBlackLCliffAndSquareUp(-100, -100)
    driveTilWhiteLCliff(-100)
    drive_timed(-100, -100, 1500)
    moveArm(c.armBotguy, 30)
    moveServo(c.servoClaw, c.clawClosed, 20)
    msleep(250)
    driveTilBlackLCliffAndSquareUp(100, 100)


def approachBotguy():
    print("approachBotguy")
    drive_timed(100, 110, 250)  #100, 105
    resetArmLowPosition()
    moveArm(c.armBotguyPickUp, 8)
    moveServo(c.servoClaw, c.clawBotguy, 12)  # was clawTram
    msleep(150)
    drive_timed(100, 110, 1550) #100, 105
    #moveArm(c.armBotguyPickUp, 5)
    moveServo(c.servoClaw, c.clawClosed, 12)
    print("Grabbed botguy")
    msleep(150)
    #Move create forward to let lego drop cubes in middle
    drive_timed(40, 40, 1000)
    ao() # let the arm rest
    msleep(30000)
    #drive to drop off botguy
    driveTilBlackLCliffAndSquareUp(-100, -100)
    msleep(300)
    driveTilWhiteLFCliff(-100)
    if c.IS_ORANGE_BOT:
        drive_timed(-100, -100, 1800)
    else:
        drive_timed(-100, -100, 1700)
    msleep(500)


def deliverBotguy():
    print("deliverBotguy")
    moveArm(c.armBotguyDelivery, 10)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(100, 100)
    driveTilWhiteLCliff(100)
    drive_timed(100, 100, 350)
    moveArm(c.armScore, 7)
    msleep(500)
    ao()
