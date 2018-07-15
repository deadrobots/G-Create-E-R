from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp
import motorz as m

colorOrder = []

cpp = None


def temp_init(icpp):
    global cpp
    cpp = icpp
    init_movement(cpp)

    m.rotate_until_stalled(20)
    msleep(1000)
    m.rotate_until_stalled(-20)
    msleep(300)
    m.set_claw_open()
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 10)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed)
    moveServo(c.servoCrateArm, c.crateArmUp)
    enable_servos()
    p.cameraInit()
    p.set_first_position(color=c.YELLOW)
    wait_for_button()
    cpp.drive_distance(-11.5, 20)
    cpp.drive_distance(2, 20)
    m.claw_to_position(c.motorMid, 25)
    cpp.drive_conditional(cpp.get_black_left, -40, state=False)
    cpp.drive_distance(-3, 50)


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
        DEBUG()  # Do not remove!!!

    selfTest()  # tests each function of the robot
    p.cameraInit()
    print("Press a button to continue")
    wait_for_button(force=True)
    # wait_4_light(c.STARTLIGHT)
    # shut_down_in(119.0)
    c.START_TIME = seconds()


def selfTest():  # separated from init for the sake of legibility
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
    # looks at first block from the side then drives to black line and line follows to the second block area
    if c.IS_BLUE_BOT:
        print("blue")
        p.set_first_position()
        m.claw_move(40)
        cpp.drive_distance(-16, 80)
        msleep(200)
        # driveTilBlackLCliffAndSquareUp(20)


def pickUpDateBinsExperiment():
    print "Picking up first date bin"
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 20)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 20)
    cpp.drive_conditional(cpp.get_bump_left, -20, state=False) # Hit center wall at tree
    cpp.drive_distance(2, 50)
    cpp.rotate(80, 20)
    cpp.drive_distance(6, 40)
    cpp.drive_distance(-8, 55)
    cpp.rotate(84, 50)
    cpp.drive_distance(6, 20) # square up
    cpp.drive_distance(-5, 50)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 25)
    m.claw_to_position(c.motorMid, 25)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 25)
    cpp.drive_distance(4, 20)
    m.claw_move(25) # close claw
    msleep(700)
    cpp.drive_distance(-11.5, 20)
    cpp.drive_distance(2, 20)
    # msleep(1000)
    m.claw_to_position(c.motorMid, 25)


def driveToSecondDateBin():
    print "Picking up second date bin"
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    # driveTilBlackLCliffAndSquareUp(-30)
    m.claw_move(40)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 15)
    cpp.rotate(90, 20)
    cpp.drive_distance(14, 50)
    cpp.rotate(-89, 20)
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    cpp.drive_distance(15, 30) # Square up infront of date bin
    cpp.drive_distance(-5, 50)
    m.claw_move(25)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 25)
    m.claw_to_position(c.motorMid, 25)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 25)
    cpp.drive_distance(4, 20)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown, 25)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown - 120, 15)
    m.claw_move(25) # close claw
    msleep(700)
    cpp.drive_distance(-11.5, 20)
    cpp.drive_distance(2, 20)
    m.claw_to_position(c.motorMid, 25)
    cpp.drive_conditional(cpp.get_black_left, -40, state=False)
    cpp.drive_distance(-3, 50)


def driveToCenterSeeding():
    print "Trying to drive to center"
    # looks at first block from the side then drives to black line and line follows to the second block area
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 10)
    moveServo(c.servoBotGuyClaw, c.clawClosed, 10)
    cpp.rotate(-90, 20)
    cpp.drive_conditional(cpp.get_black_right, -40, state=False)
    cpp.drive_distance(-4, 40)
    p.set_second_position()
    p.set_final_positions()


def getCrates():  # break this function into smaller bites... make driveToCrates, getCrates, turnAround,etc
    print "Picking up crates"
    # drives center area grabs cube and turns around to prep for botguy grab
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 10)
    cpp.rotate(-90, 20)
    cpp.drive_distance(-4.5, 20)
    driveTilBlackLCliffAndSquareUp(10)
    # moveServo(c.servoCrateArm, c.crateArmGrab, 20)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    moveServo(c.servoCrateArm, c.crateArmDown, 20)
    cpp.drive_distance(-5.5, 30)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    driveTilBlackLCliffAndSquareUp(50)
    # cpp.drive(0, 0)
    cpp.drive_distance(2, 20)
    moveServo(c.servoCrateArm, c.crateArmUp, 10)
    cpp.rotate(90, 30)
    cpp.drive_distance(3, 30) #2
    cpp.rotate(90, 30)


def getBotGuy():
    print "Picking up Botguy"
    # grabs botguy and backs out of area
    m.claw_move(40)
    driveTilBlackLCliffAndSquareUp(20)
    msleep(500)
    cpp.drive_distance(-2.5, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)
    driveTilBlackLCliffAndSquareUp(20)
    msleep(500)
    cpp.drive_distance(3, 35)
    m.claw_to_position(c.motorMid, 20)
    msleep(500)
    cpp.drive_distance(7.5, 25)
    msleep(500)
    m.claw_move(40)
    msleep(1000)
    cpp.drive_distance(-15, 35)
    moveServo(c.servoCrateArm, c.crateArmUp, 15)


def driveToYellow():
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
    # delivers crates when yellow block is in first zone
    cpp.drive_distance(-4, 35)
    lineFollowLeftFrontTilRightFrontBlack(250)
    cpp.drive_distance(1, 30)
    cpp.rotate(-90, 35)
    cpp.drive_distance(17.5, 35)
    cpp.rotate(90, 35)
    driveTilBlackLCliffAndSquareUp(30)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 15)
    cpp.drive_distance(-12.5, 35)
    # Drop blocks below
    cpp.drive_distance(3, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    cpp.drive_distance(-4, 35)
    cpp.drive_distance(12.5, 25)
    cpp.rotate(-90, 35)
    cpp.drive_distance(12, 30)
    cpp.rotate(88, 35)
    cpp.drive_distance(-9, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmUp)
    cpp.drive_distance(-4, 35)
    # driving back to center after dropping off crates
    cpp.drive_distance(18, 30)
    cpp.drive_conditional(black_left_or_right, -30, state=False)
    driveTilBlackLCliffAndSquareUp(-30)
    cpp.rotate(90, 30)
    cpp.drive_conditional(cpp.get_black_left, 30, state=False)
    cpp.drive_distance(-3, 40)
    cpp.rotate(90, 30)


def goYellowSecond():
    print "Yellow is in second position"
    cpp.rotate(21, 30)  #15
    cpp.drive_distance(-8, 15)
    # Deliver Blocks
    cpp.drive_distance(3, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    cpp.drive_distance(-4, 50)
    cpp.drive_distance(4, 50)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    cpp.rotate(-40, 30)
    cpp.drive_distance(-2, 30)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15 )
    moveServo(c.servoCrateArm, c.crateArmUp)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    cpp.drive_distance(-4, 50)
    moveServo(c.servoCrateArm, c.crateArmVeryHigh, 20)
    cpp.drive_distance(5, 30)
    cpp.rotate(30, 40)
    # drive back to the center position to then go and drop off bot guy
    cpp.drive_distance(13, 40)
    cpp.rotate(180, 30)
    driveTilBlackLCliffAndSquareUp(30)
    cpp.drive_distance(-4, 40)


def goYellowThird():
    print "Yellow is in third position"
    # if yellow cube is in third zone (farthest from startbox)
    cpp.drive_distance(-4, 35)
    lineFollowLeftFrontTilRightFrontBlack(250)
    cpp.drive_distance(1, 30)
    cpp.rotate(90, 35)
    cpp.drive_distance(16, 35)
    cpp.rotate(-90, 35)
    driveTilBlackLCliffAndSquareUp(30)
    cpp.drive_distance(-12.5, 35)
    # Drop blocks below
    cpp.drive_distance(2.5, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 10)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 10)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 10)
    cpp.drive_distance(-4, 35)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 10)
    cpp.drive_distance(14, 25)
    cpp.rotate(90, 35)
    cpp.drive_distance(10.5, 30)
    cpp.rotate(-90, 35)
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    cpp.drive_distance(-9, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 10)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 10)
    moveServo(c.servoCrateArm, c.crateArmDeStack)   #not actually detacking, just need value to move under cog railway
    cpp.drive_distance(-2.5, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 10)
    cpp.drive_distance(11, 30)
    # driving back to the center to then go and drop off bot guy
    cpp.drive_distance(8, 30)
    cpp.drive_conditional(black_left_or_right, -30, state=False)
    driveTilBlackLCliffAndSquareUp(-30)
    cpp.rotate(-90, 30)
    cpp.drive_conditional(cpp.get_black_right, 30, state=False)
    cpp.drive_distance(-3, 40)
    cpp.rotate(-90, 30)


def driveToRed():  # Starts from the middle or it won't work and that's not our fault!
    print "Driving to red"
    position = p.get_positions()
    if position[1] == c.RED:
        print('one')
        goRedFirst()
    elif position[2] == c.RED:
        print('two')
        goRedSecond()
    elif position[3] == c.RED:
        print('three')
        goRedThird()
    else:
        print('im dum')


def goRedFirst(): # when red is in first position drop botguy off there
    cpp.rotate(90, 30)
    cpp.drive_distance(18, 30)
    cpp.rotate(-90, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=False)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=True)
    cpp.drive_distance(2, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)


def goRedSecond():  # when red is in second position drop botguy off there
    cpp.rotate(10, 40)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=False)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=True)
    cpp.drive_distance(2, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 5)


def goRedThird():  # when red is in third position drop botguy off there
    cpp.rotate(-90, 30)
    cpp.drive_distance(16, 30) #15
    cpp.rotate(90, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=False)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=True)
    cpp.drive_distance(2, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)
