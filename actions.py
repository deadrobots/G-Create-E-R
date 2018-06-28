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
    selfTestDateGrab()
    p.cameraInit()
    print("Press right button to continue")
    wait_for_button()
    #wait_4_light(c.STARTLIGHT)
    shut_down_in(119.0)
    print("Running the robot.")
    c.START_TIME = seconds()

def selfTestDateGrab(): #Are we using this function anymore? Can we delete it?
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
    drive_timed(100, 100, 2500)
    msleep(250)
    drive_timed(-100, -100, 2500)
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

def pickUpDateBinsExperiment(): #Are we using this function anymore? Can we delete it?
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    driveTillBump(-125, -100)
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


def getOutOfStartBoxSeeding():
    #looks at first block from the side then drives to black line and line follows to the second block area
    if c.IS_BLUE_BOT:
        seeBlocksWithoutOrange()
        msleep(1000)
        driveTilBlackLCliffAndSquareUp(-250, -230)
    elif c.IS_GREEN_BOT:
        seeBlocksWithoutOrange()
        drive_timed(-100, -100, 3300)
        rotate_degrees(80, 100)
        msleep(1000)

def getOutOfStartBoxAndDriveToCenter():
    print ("Driving out of start box and going to center")
    seeBlocksWithoutOrange()
    msleep(1000)
    drive_timed(-130, -100, 3250)
    rotateTillBlack(100)
    lineFollowRightFrontTilBlack()
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

def driveToCenterSeeding():
    #looks at first block from the side then drives to black line and line follows to the second block area
    if c.IS_BLUE_BOT:
        lineFollowRightFrontTilBlack()
        drive_timed(-50, -50, 1000)
    elif c.IS_GREEN_BOT:
        lineFollowRightFrontTilBlack()
        drive_timed(-50, -50, 1000)

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
    #drives center area grabs cube and turns around to prep for botguy grab
    if c.IS_BLUE_BOT:
        rotate_degrees(-90, 200)
        drive_timed(75, 75, 1000)
        msleep(1000)
        driveTilBlackLCliffAndSquareUp(-75,-75) #end of func. 1
        # rotate_degrees(1, 50)
        moveServo(c.servoCrateArm, c.crateArmDown, 15)
        moveServo(c.servoCrateClaw, c.crateGrab, 15)
        msleep(500)
        drive_timed(-100, -80, 1600)
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
    elif c.IS_GREEN_BOT:
        rotate_degrees(-90,200)
        drive_timed(75,75, 2000)
        msleep(450)
        driveTilBlackLCliffAndSquareUp(-75,-75)
        moveServo(c.servoCrateArm, c.crateArmDown, 15)
        moveServo(c.servoCrateClaw, c.crateClawOpen, 15)
        msleep(200)
        drive_timed(-100, -100, 700)
        drive_timed(-75, -75, 1350)
        # drive_timed(-75, -75, 100)
        msleep(100)
        moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
        moveServo(c.servoCrateArm, c.crateArmMid, 15)
        msleep(350)
        driveTilBlackLCliffAndSquareUp(100, 100)
        moveServo(c.servoCrateArm, c.crateArmMid, 15)
        rotate_degrees(180, 100) #180
        msleep(500)
        moveServo(c.servoBotGuyClaw, c.clawBotguy, 15)

def getBotGuy():
    # grabs botguys and backs out of area
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    driveTilBlackLCliffAndSquareUp(100, 100)
    if c.IS_BLUE_BOT:
        timedLineFollowFrontTophat(0.4)
        moveServo(c.servoBotGuyClaw, c.clawbotguyArea, 10)
        timedLineFollowFrontTophat(2.2)
    else:
        drive_timed(100, 100, 200)
        msleep(250)
        drive_timed(100, 100, 300)
        msleep(100)
        drive_timed(120, 100, 1500)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)  # grab botguy
    driveTilBlackLCliffAndSquareUp(-100, -100)
    drive_timed(-100, -100, 1000)
    msleep(500)

def gotoSecondBlock(): #can we delete this?
    print "gotoSecondBlock"
    rotate_degrees(-80, 100)

def dropBlocks(): #can we break this function up?
    if c.IS_GREEN_BOT:
        rotate_degrees(113, 150)
        drive_timed(-75, -75, 1500)
    elif c.IS_BLUE_BOT:
        # rotate_degrees(-25, 150)
        drive_timed(-75, -75, 1150)
        rotate_degrees(5, 56)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    # if colorOrder[0] == c.YELLOW:         #can we get rid of this?
    #     drive_timed(-60, -60, 1500)
    #     drive_timed(60, 60, 1500)
    # elif colorOrder[1] == c.YELLOW:
    #     drive_timed(-60, -60, 900)
    #     drive_timed(60, 60, 900)
    # elif colorOrder[2] == c.YELLOW:
    #     drive_timed(-60, -60, 1100)
    #     drive_timed(60, 60, 1100)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    drive_timed(120, 100, 1500)
    rotate_degrees(80, 100)
    timedLineFollowLeftFront(100, 2.8)
    rotate_degrees(-80, 100)
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

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()

def goYellowFirst():
    #delivers crates when yellow block is in first zone
    if c.IS_GREEN_BOT:
        rotate_degrees(90, 100)
        timedLineFollowLeftFront(250, 2.5)
        rotate_degrees(-65, 60)
        drive_timed(-50, -50, 2900)
        rotate_degrees(2, 70)
        moveServo(c.servoCrateArm, c.crateArmAlmostDown)
        moveServo(c.servoCrateClaw, c.crateClawOpen)
        moveServo(c.servoCrateArm, c.crateArmDeStack)
        moveServo(c.servoCrateClaw, c.crateClawClosed)
        moveServo(c.servoCrateArm, c.crateArmLiftCrate)
        drive_timed(-80, -80, 700)
        drive_timed(80, 80, 1500)
        rotate_degrees(-35, 70)
        moveServo(c.servoCrateArm, c.crateArmDown)
        moveServo(c.servoCrateClaw, c.crateClawOpen)
        moveServo(c.servoCrateArm, c.crateArmUp)
        drive_timed(-80, -80, 1800)
        msleep(7000)
    elif c.IS_BLUE_BOT:
        rotate_degrees(90, 100)
        lineFollowLeftFrontTilRightFrontBlack(250)
        rotate_degrees(-85,100)
        driveTilFrontTophatBlack(-100,-100)

def goYellowSecond():
    #if yellow cube is in middle area
    turnTilRightFrontBlack(100,-100)
    drive_distance(-3,100)
    rotate_degrees(87, 100)
    driveTilFrontTophatBlack(-100,-100)

def goYellowThird():
    #if yellow cube is in third zone (farthest from startbox)
    if c.IS_GREEN_BOT:
        pass
    elif c.IS_BLUE_BOT:
        rotate_degrees(-95, 100)
        lineFollowRightFrontTilLeftFrontBlack(250)
        rotate_degrees(85, 100)
        driveTilFrontTophatBlack(-100, -100)
