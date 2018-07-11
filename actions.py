from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp
import motorz as m

colorOrder = []

cpp = None

def init(icpp):
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
    global cpp
    cpp = icpp
    init_movement(cpp)
    init_utilities(cpp)
    if c.IS_BLUE_BOT:
        print("I AM BLUE")
    elif c.IS_GREEN_BOT:
        print("I AM GREEN!")
    else:
        print("Check clone switch")
        DEBUG() # Do not remove!!!
    selfTest()  #tests each function of the robot
    p.cameraInit()
    print("Press a button to continue")
    wait_for_button()
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
    m.rotate_until_stalled(20)
    msleep(1000)
    m.rotate_until_stalled(-20)
    msleep(300)
    m.set_claw_open()
    # test drive
    cpp.drive_timed(-20, -20, 2500)
    msleep(250)
    cpp.drive_timed(20, 20, 2500)
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


def centerPipeRunAndBotGuyGrab():
    print ("Heading to Botguy test")
    p.set_first_position()
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)
    m.rotate_until_stalled(20)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 15)
    cpp.rotate(25, 50)
    cpp.drive_distance(35, 50)
    cpp.drive_distance(8, 20)
    cpp.drive_distance(-2,50)
    cpp.rotate(83, 50)
    cpp.drive_distance(5,25)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 30)
    m.claw_to_position(c.clawBotguy, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    cpp.drive_distance(9, 30)
    m.claw_move(40)
    msleep(3000)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 5)


def headToSecondBlock():
    print ("Heading to second block!")
    cpp.drive_distance(-6,25)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 5)
    cpp.rotate(90,50)
    driveTilBlackLRCliffAndSquareUp(50,50)
    cpp.rotate(-90,50)
    cpp.drive_conditional(cpp.get_black_left, 40, state=False)
    cpp.drive_distance(-1.5, 40)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 5)
    #cpp.drive_distance(-3.5, 40)


def getCrates():
    print "Picking up crates"
    #drives center area grabs cube
    p.set_second_position()
    p.set_final_positions()
    cpp.rotate(85, 20)
    msleep(1000)
    cpp.drive_conditional(black_left_or_right, -20, state=True)     #work on fixing alignment here
    driveTilBlackLCliffAndSquareUp(-15,-15) #end of func. 1
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    #timedLineFollowRightFront(-20,2)
    cpp.drive_distance(-6.5, 40)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates # end of func.2
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    msleep(500)
    cpp.drive_distance(8, 40)
    moveServo(c.servoCrateArm, c.crateArmMid+200, 2)

def driveToYellow(): # Needs to start from the middle or it won't work
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
    #rotate_degrees(-90, 100)
    lineFollowLeftFrontTilRightFrontBlack(-50)
    wait_for_button()
    cpp.rotate(-85,100) #update to cpp.rotate
    driveTilFrontTophatBlack(-20,-20)
    cpp.rotate(-90,35)  #update to cpp.rotate
    cpp.drive_distance(-9,35)
    cpp.rotate(90,35) #update to cpp.rotate
    driveTilBlackLCliffAndSquareUp(-30,-30)
    cpp.drive_distance(7.5,35)


def goYellowSecond():
    print "Yellow is in second position"
    #if yellow cube is in middle area
    turnTilRightFrontBlack(-20,20)
    cpp.drive_distance(3,100)
    cpp.rotate(87, 100) #update to cpp.rotate
    driveTilFrontTophatBlack(20,20)


def goYellowThird():
    print "Yellow is in third position"
    #if yellow cube is in third zone (farthest from startbox)
    cpp.rotate(-85, 100)    #update to cpp.rotate
    lineFollowRightFrontTilLeftFrontBlack(-50)
    cpp.rotate(85, 100) #update to cpp.rotate
    driveTilFrontTophatBlack(20, 20)


def dropBlocks():
    print "Delivering crates"
    rotate(-5,25)   #update to cpp.rotate
    cpp.drive_distance(-1.5,35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    cpp.drive_distance(1.5,35) #backup not currently working
    rotate(90,35)   #update to cpp.rotate
    cpp.drive_distance(-11.5,25)
    rotate(-90,35)  #update to cpp.rotate
    wait_for_button()
    cpp.drive_timed(120, 100, 1400)
    moveServo(c.servoCrateArm, c. crateArmDown)
    moveServo(c.servoCrateClaw, c.crateClawOpen)
    cpp.drive_timed(-120, -100, 1400)
    DEBUG()
    msleep(500)
    # drive_timed(-60, -60, 1500)
    rotate(35, 40)     #update to cpp.rotate
    cpp.drive_timed(60, 60, 1500)
    # drive_timed(75, 75, 1200)
    # rotate_degrees(35, 65) #40
    # drive_timed(-75, -75, 1400)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    if colorOrder[0] == c.YELLOW:
        cpp.rotate(-15, 56) #update to cpp.rotate
    # elif colorOrder[1] == c.YELLOW:
    elif colorOrder[2] == c.YELLOW:
        cpp.rotate(-8, 56)  #update to cpp.rotate
    cpp.drive_timed(100, 100, 900)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen-200, 10)
    moveServo(c.servoCrateArm, c.crateArmUp, 10)
    cpp.drive_timed(-80, -80, 2000)
