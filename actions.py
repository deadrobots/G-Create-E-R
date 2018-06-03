from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p


colorOrder = []

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
    elif c.IS_GREEN_BOT:
        print("I AM GREEN!")
    else:
        print("I AM YELLOW")
        DEBUG() # Do not remove!!!
    #DEBUG()
    ################################
    selfTestDateGrab()
    ################################
    #p.cameraInit()
    print("Press right button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    shut_down_in(119.0)
    print("Running the robot.")
    c.START_TIME = seconds()

def selfTest():
    #tests all motors and servos
    # raise arm
    print ("Running Self Test")
    testArm()
    resetArm(30, 2000)
    # open/close claw
    enable_servo(c.servoBotGuyClaw)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    # lower ramp
    enable_servo(c.servoHayArm)
    moveServo(c.servoHayArm, c.hayArmDown, 10)
    enable_servo(c.servoHayClaw)
    moveServo(c.servoHayClaw, c.hayClawClosed, 10)
    moveServo(c.servoHayClaw, c.hayClawOpen, 10)
    moveServo(c.servoHayArm, c.hayArmUp, 10)
    # lower the arm
    moveArm(c.armStartbox, 30)
    ao()
####################################################################
def selfTestDateGrab():
    print ("Running Self Test")
    enable_servo(c.servoBotGuyArm)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    msleep(1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    # open/close claw
    enable_servo(c.servoBotGuyClaw)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyClaw, c.clawStart, 15)
    # test drive
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
    # lower ramp
    enable_servo(c.servoCrateArm)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    enable_servo(c.servoCrateClaw)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmUp, 10)

    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    ao()

def pickUpDateBinsExperiment():
    #drive from start box to date bin
    #drive_timed(-160, -160, 1400)
    #rotate_degrees(86, 100)
    #drive_timed(250, 250, 1800)

    drive_timed(-250, -250, 1100)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown-150, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    drive_timed(-40, -40, 3600)
    # msleep(1000)
    moveServo(c.servoBotGuyClaw, c.clawLoose, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    drive_timed(100, 100, 1800)


####################################################################3
def getOutOfstartBox ():
    rotate_degrees(-28, 100)
    if c.IS_BLUE_BOT:
        drive_timed(-100, -100, 3000)
        rotate_degrees(90, 100)
        timedLineFollowRightFront(250, 4.85)
    elif c.IS_GREEN_BOT:
        drive_timed(-100, -100, 3200)
        rotate_degrees(75, 100)
        msleep(2000)
        timedLineFollowRightFront(250, 4.65)


def seeBlocks():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToSecondBlock():
    timedLineFollowRightFront(200, 3.2)

def getCrates():
    if c.IS_BLUE_BOT:
        rotate_degrees(-90,200)
        drive_timed(75,75, 2000)
        msleep(1000)
        driveTilBlackLCliffAndSquareUp(-75,-75)
        moveServo(c.servoHayArm, c.hayArmDown, 10)
        moveServo(c.servoHayClaw, c.hayClawOpen, 10)
        msleep(250)
        drive_timed(-100, -100, 400)
        resetArm(30, 2000)
        drive_timed(-65, -75, 1450)
        moveServo(c.servoHayClaw, c.hayClawClosed, 10)
        msleep(500)
        driveTilBlackLCliffAndSquareUp(250,250)
        moveServo(c.servoHayArm, c.hayArmCarry, 10)
        rotate_degrees(180, 100)
        msleep(1000)
        moveServo(c.servoBotGuyClaw, c.clawBotguy, 10)
    elif c.IS_GREEN_BOT:
        rotate_degrees(-90,200)
        drive_timed(75,75, 2000)
        msleep(750)
        driveTilBlackLCliffAndSquareUp(-75,-75)
        moveServo(c.servoCrateArm, c.crateArmDown, 10)
        moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
        msleep(250)
        drive_timed(-100, -100, 700)
        drive_timed(-75, -55, 1000)
        drive_timed(-75, -75, 800)
        msleep(100)
        moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
        msleep(500)
        driveTilBlackLCliffAndSquareUp(100, 100)
        moveServo(c.servoCrateArm, c.crateArmMid, 10)
        rotate_degrees(180, 100)
        msleep(1000)
        moveServo(c.servoBotGuyClaw, c.clawBotguy, 10)


def getBotGuy():
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 10)
    driveTilBlackLCliffAndSquareUp(250,250)
    moveServo(c.servoBotGuyClaw, c.clawbotguyArea, 10)
    msleep(500)
    drive_timed(100, 100, 500)
    msleep(100)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    driveTilBlackLCliffAndSquareUp(-100, -100)
    drive_timed(-100, -100, 1500)
    msleep(1000)


def gotoSecondBlock():
    moveArm(c.armUpbotguy, 40)
    rotate_degrees(-80, 100)



def seeBlocks2():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
        dropBlocksFirst()
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")

def goToBlock3():
    timedLineFollowRightFrontBlocks(200, 3)


def seeBlocks3():
    s = p.checkColor(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
    p.determineOrder(colorOrder)


def dropBlocksFirst():
    rotate_degrees(70 , 150)
    moveServo(c.servoHayArm, c.hayArmDown, 10)
    moveServo(c.servoHayClaw, c.hayClawOpen, 10)
    drive_timed(-75, -75, 750)


