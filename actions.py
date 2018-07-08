from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp

colorOrder = []

cpp = None

def init(icpp):
    '''For Setup:
    Make sure that both bumpers are touching the back edges of the starting box
    Point the "arm" at the opposite corner of starting box (intersection of black tape)
    Use pencil marks on table to check alignment
    Line up the block of wood with the straight line to perfect the setup'''
    global cpp
    cpp = icpp
    init_movement(cpp)


    print("Create connected...")
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
    wait_for_button(force=True)
    #wait_4_light(c.STARTLIGHT)
    # shut_down_in(119.0)
    c.START_TIME = seconds()

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
    cpp.drive_distance(10, 40)
    msleep(250)
    cpp.drive_distance(-10, 40)
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
    if c.IS_BLUE_BOT:
        print("blue")
        p.set_first_position()
        cpp.drive_distance(-16, 80)
        msleep(200)
        # driveTilBlackLCliffAndSquareUp(20)


def pickUpDateBinsExperiment():
    print "Picking up first date bin"
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    cpp.drive_conditional(cpp.get_bump_left, -20, state=False)
    cpp.drive_distance(2, 50)
    cpp.rotate(80, 20)
    cpp.drive_distance(6, 40)
    cpp.drive_distance(-8, 55)
    cpp.rotate(84, 50)
    cpp.drive_distance(6, 20)
    cpp.drive_distance(-5, 50)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    cpp.drive_distance(4, 20)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    cpp.drive_distance(-11.5, 10)
    cpp.drive_distance(2, 10)
    # msleep(1000)
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
    # driveTilBlackLCliffAndSquareUp(-30)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    cpp.rotate(90, 20)
    cpp.drive_distance(14, 50)
    cpp.rotate(-89, 20)
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    cpp.drive_distance(15, 30)
    cpp.drive_distance(-5, 50)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    cpp.drive_distance(4, 20)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    cpp.drive_distance(-11.5, 10)
    cpp.drive_distance(2, 10)
    moveServo(c.servoBotGuyClaw, c.clawMid, 10)
    cpp.drive_conditional(cpp.get_black_left, -40, state=False)
    cpp.drive_distance(-3, 50)
    # cpp.drive_distance(-5, 30)
    # moveServo(c.servoBotGuyArm, c.botGuyArmMid, 15)
    # moveServo(c.servoBotGuyClaw, c.clawMid, 15)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    # cpp.drive_distance(4, 20)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    # moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    # cpp.drive_distance(-11.5, 10)
    # cpp.drive_distance(2, 10)
    # moveServo(c.servoBotGuyClaw, c.clawMid, 10)

def driveToCenterSeeding():
    print "Trying to drive to center"
    #looks at first block from the side then drives to black line and line follows to the second block area
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 10)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    cpp.rotate(-90, 20)
    cpp.drive_conditional(cpp.get_black_right, -40, state=False)
    cpp.drive_distance(-1.5, 40)
    p.set_second_position()
    p.set_final_positions()


def getCrates(): #break this function into smaller bites... make driveToCrates, getCrates, turnAround,etc
    print "Picking up crates"
    #drives center area grabs cube and turns around to prep for botguy grab
    cpp.rotate(-90, 20)
    cpp.drive_distance(-4, 20)
    driveTilBlackLCliffAndSquareUp(10)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    wait_for_button()
    cpp.drive_distance(-5, 30)
    # rotate(2,50)
    # msleep(500)
    # drive_timed(-100, -80, 1600)
    # drive_timed(-100, -100, 500) #400
    # drive_timed(-100, -85, 1100)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates # end of func.2
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    wait_for_button()
    driveTilBlackLCliffAndSquareUp(50)
    # cpp.drive(0, 0)
    wait_for_button()
    cpp.drive_distance(2, 20)
    moveServo(c.servoCrateArm, c.crateArmMid+200, 2)
    cpp.rotate(180, 30)
    driveTilBlackLCliffAndSquareUp(-10)
    msleep(1000)
    DEBUG()
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
    position = p.get_positions()
    if position[1] == c.YELLOW:
        goYellowFirst()
    elif position[2] == c.YELLOW:
        goYellowSecond()
    elif position[3] == c.YELLOW:
        goYellowThird()

def goYellowFirst():
    print "Yellow is in first position"
    #delivers crates when yellow block is in first zone
    if c.IS_GREEN_BOT:
        cpp.rotate(90, 100)
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
        cpp.rotate(90, 100)
        lineFollowLeftFrontTilRightFrontBlack(250)
        cpp.rotate(-85,100)
        driveTilFrontTophatBlack(-100,-100)
        cpp.rotate(-90,35)
        cpp.drive_distance(9,35)
        cpp.rotate(90,35)
        driveTilBlackLCliffAndSquareUp(150,150)
        cpp.drive_distance(7.5,35)


def goYellowSecond():
    print "Yellow is in second position"
    #if yellow cube is in middle area
    turnTilRightFrontBlack(100,-100)
    cpp.drive_distance(-3,100)
    cpp.rotate(90, 100)
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
    if c.IS_GREEN_BOT:
        rotate_degrees(113, 150)
        drive_timed(-75, -75, 1500)
    elif c.IS_BLUE_BOT:
        rotate(-5,25)
        cpp.drive_distance(1.5,35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    cpp.drive_distance(-1.5,35) #backup not currently working
    rotate(90,35)
    cpp.drive_distance(11.5,25)
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
