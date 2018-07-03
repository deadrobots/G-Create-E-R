from movement import *
from utilities import *
from createPlusPlus import drive_distance, rotate, pivot_on_left, pivot_on_right
from createPlusPlus import drive_timed as new_drive_timed
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
    # create_disconnect()
    # if not create_connect_once():
    #     print("Create not connected...")
    #     exit(0)
    # print("Create connected...")
    # create_full()
    cpp.connect()
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE")
    elif c.IS_GREEN_BOT:
        print("I AM GREEN!")
    else:
        print("I AM YELLOW")
        DEBUG() # Do not remove!!!
    selfTest()  #tests each function of the robot
    p.cameraInit()
    print("Press a button to continue")
    #wait_4_light(c.STARTLIGHT)
    # shut_down_in(119.0)
    c.START_TIME = seconds()

def centerPipeRunTest():
    cpp.connect()
    cpp.rotate(35, 50)
    cpp.drive_distance(-42, 50)
    cpp.drive_distance(1.5,50)
    cpp.rotate(90, 75)
    cpp.drive_distance(-11, 50)
    cpp.disconnect()
    exit(0)
    DEBUG


def selfTest(): #separated from init for the sake of legibility
    print ("Running Self Test")
    enable_servo(c.servoBotGuyArm)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    msleep(500)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    # open/close claw
    enable_servo(c.servoBotGuyClaw)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyClaw, c.clawStart, 15)
    # test drive
    cpp.drive_timed(20, 20, 2500)
    msleep(250)
    cpp.drive_timed(-20, -20, 2500)
    # lower ramp
    enable_servo(c.servoCrateArm)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    enable_servo(c.servoCrateClaw)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateClaw, c.crateClawStart, 10)
    moveServo(c.servoCrateArm, c.crateArmStart, 10)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 15)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    ao()

def getOutOfStartBoxSeeding():
    print "Going to Date bin"
    #looks at first block from the side then drives to black line and line follows to the second block area
    seeBlocksWithoutOrange()
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(-250, -230)

def pickUpDateBinsExperiment():
    print "Picking up first date bin"
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    driveTillBump(-125, -100)   #corrected "mirroring" with negative values; see function declaration
    drive_timed(100, 80, 700)
    rotate_degrees(80, 100)
    drive_timed(100, 80, 1500)
    drive_timed(-150, -130, 1700)
    rotate_degrees(84, 100)
    drive_timed(110, 100, 1500)
    drive_timed(-115, -100, 1500)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    drive_timed(-60, -40, 5000)
    # msleep(1000)
    drive_timed(65, 50, 700)
    moveServo(c.servoBotGuyClaw, c.clawMid, 10)
    # driveTilBlackLCliffAndSquareUp(-250, -230)
    # rotate_degrees(4, 100)
    # drive_timed(110, 100, 4600)
    # drive_timed(-115, -100, 1500)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    # moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    # moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    # drive_timed(100, 100, 1500)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown-120, 15)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    # drive_timed(-60, -40, 5000)
    # # msleep(1000)
    # drive_timed(65, 50, 700)
    # moveServo(c.servoBotGuyClaw, c.clawMid, 10)

def driveToSecondDateBin():
    print "Picking up second date bin"
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    driveTilBlackLCliffAndSquareUp(-150, -150)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    rotate_degrees(-80, 100)
    timedLineFollowLeftFront(200, 2)
    rotate_degrees(80, 100)
    drive_timed(115, 100, 1000)
    driveTilBlackLCliffAndSquareUp(-150, -150)
    drive_timed(120, 100, 4600)
    drive_timed(-115, -100, 1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    drive_timed(100, 100, 1500)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    drive_timed(-60, -40, 5000)
    drive_timed(65, 50, 700)
    moveServo(c.servoBotGuyClaw, c.clawMid, 10)
    driveTilBlackLCliffAndSquareUp(-150, -150)
    rotate_degrees(-80, 100)

def driveToCenterSeeding():
    print "Trying to drive to center"
    #looks at first block from the side then drives to black line and line follows to the second block area
    lineFollowRightFrontTilRightBlack()
    drive_timed(-50, -50, 1000)

def getOutOfStartBoxAndDriveToCenter():
    print ("Driving out of start box and going to center")
    seeBlocksWithoutOrange()
    msleep(1000)
    drive_timed(-130, -100, 3250)
    rotateTillBlack(100)
    lineFollowRightFrontTilRightBlack()
    drive_timed(-50, -50, 1000)


# def driveToCenter():
#     if c.IS_BLUE_BOT:
#         rotate_degrees(80, 100)
#         lineFollowRightFrontTilBlack()
#         drive_timed(-50, -50, 1000)
#     elif c.IS_GREEN_BOT:
#         rotate_degrees(80, 100)
#         lineFollowRightFrontTilBlack()
#         drive_timed(-50, -50, 1000)

def seeBlocksWithoutOrange():
    #allows robot to check color of first cube from the startbox
    s = p.checkColorWithoutOrange(colorOrder)
    print(get_object_area(c.YELLOW, 0))
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube (Without Orange)")

def seeBlocks():
    #allows robot to determine color of second cube and then determine color of third cube
    s = p.checkColor(colorOrder)
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
    p.determineOrder(colorOrder)

def getCrates(): #break this function into smaller bites... make driveToCrates, getCrates, turnAround,etc
    print "Picking up crates"
    #drives center area grabs cube and turns around to prep for botguy grab
    rotate_degrees(-90, 200)
    drive_timed(75, 75, 1000)
    msleep(1000)
    driveTilBlackLCliffAndSquareUp(-75,-75) #end of func. 1
    # rotate_degrees(1, 50)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    timedLineFollowRightFront(100,1.6)
    # rotate(2,50)
    # msleep(500)
    # drive_timed(-100, -80, 1600)
    # drive_timed(-100, -100, 500) #400
    # drive_timed(-100, -85, 1100)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates # end of func.2
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    msleep(500)
    driveTilBlackLCliffAndSquareUp(250,250)
    moveServo(c.servoCrateArm, c.crateArmMid+200, 2)
    rotate_degrees(155, 50)  #145
    msleep(1000)
    moveServo(c.servoBotGuyClaw, c.clawBotguy, 15)


def getBotGuy():
    print "Picking up Botguy"
    # grabs botguys and backs out of area
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    driveTilBlackLCliffAndSquareUp(100, 100)
    timedLineFollowFrontTophat(0.4)
    moveServo(c.servoBotGuyClaw, c.clawbotguyArea, 10)
    timedLineFollowFrontTophat(2.7)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)  # grab botguy
    driveTilBlackLCliffAndSquareUp(-100, -100)
    drive_timed(-100, -100, 1000)
    msleep(500)

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    print "Driving to yellow"
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()

def goYellowFirst():
    print "Yellow is in first position"
    #delivers crates when yellow block is in first zone
    rotate_degrees(90, 100)
    lineFollowLeftFrontTilRightFrontBlack(250)
    rotate_degrees(-85,100)
    driveTilFrontTophatBlack(-100,-100)
    rotate(-90,35)
    drive_distance(9,35)
    rotate(90,35)
    driveTilBlackLCliffAndSquareUp(150,150)
    drive_distance(7.5,35)


def goYellowSecond():
    print "Yellow is in second position"
    #if yellow cube is in middle area
    turnTilRightFrontBlack(100,-100)
    drive_distance(-3,100)
    rotate_degrees(87, 100)
    driveTilFrontTophatBlack(-100,-100)

def goYellowThird():
    print "Yellow is in third position"
    #if yellow cube is in third zone (farthest from startbox)
    rotate_degrees(-85, 100)
    lineFollowRightFrontTilLeftFrontBlack(250)
    rotate_degrees(85, 100)
    driveTilFrontTophatBlack(-100, -100)

def dropBlocks(): #can we break this function up?
    print "Delivering crates"
    rotate(-5,25)
    drive_distance(1.5,35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    drive_distance(-1.5,35) #backup not currently working
    rotate(90,35)
    drive_distance(11.5,25)
    rotate(-90,35)
    wait_for_button()
    drive_timed(-120, -100, 1400)
    moveServo(c.servoCrateArm, c. crateArmDown)
    moveServo(c.servoCrateClaw, c.crateClawOpen)
    drive_timed(120, 100, 1400)
    DEBUG()
    msleep(500)
    # drive_timed(-60, -60, 1500)
    rotate_degrees(35, 40)
    drive_timed(-60, -60, 1500)
    if c.IS_GREEN_BOT:
        drive_timed(75, 75, 1500)
        rotate_degrees(40, 65) #40
        drive_timed(-75, -75, 1500)
    elif c.IS_BLUE_BOT:
        # drive_timed(75, 75, 1200)
        # rotate_degrees(35, 65) #40
        # drive_timed(-75, -75, 1400)
        moveServo(c.servoCrateArm, c.crateArmDown, 10)
        if colorOrder[0] == c.YELLOW:
            rotate_degrees(-15, 56)
        # elif colorOrder[1] == c.YELLOW:
        elif colorOrder[2] == c.YELLOW:
            rotate_degrees(-8, 56)
        drive_timed(-100, -100, 900)
        moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen-200, 10)
        moveServo(c.servoCrateArm, c.crateArmUp, 10)
        drive_timed(80, 80, 2000)
