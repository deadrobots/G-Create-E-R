from movement import *
from utilities import *
import constants as c
from wallaby import *
import camera as p
import createPlusPlus as cpp
import motorz as m
import multiprocessing

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
    wait_for_button_blink()
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
    cpp.drive_distance(-6, 20)
    msleep(250)
    cpp.drive_distance(6, 20)
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
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown)
    # m.rotate_until_stalled(20)
    multiprocessing.Process(target=moveServo, args=(c.servoBotGuyArm, c.botGuyArmStart, 15)).start()
    multiprocessing.Process(target=m.rotate_until_stalled, args=(20,)).start()
    # multiprocessing.Process(target=function)
    # multiprocessing.Process(target=function)
    cpp.rotate(35, 20)
    cpp.drive_distance(35, 60)
    cpp.drive_distance(6, 20)
    cpp.drive_distance(3, 10)
    cpp.drive_distance(-2, 50)
    cpp.rotate(75, 50)
    cpp.drive_distance(6, 25)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp, 30)
    m.claw_to_position(c.clawBotguy, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 15)
    cpp.drive_distance(6, 30)
    m.claw_move(40)
    msleep(1000)
    moveServo(c.servoBotGuyArm, c.botGuyArmMid, 5)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 20)


def headToSecondBlock():
    print ("Heading to second block!")
    cpp.drive_distance(-6, 25)
    moveServo(c.servoBotGuyArm, c.botGuyArmStart, 5)
    cpp.rotate(90,20)
    squareUpOnBlack(50)
    cpp.rotate(-90,20)
    cpp.drive_conditional(cpp.get_black_left, 40, state=False)
    cpp.drive_distance(-2.5, 40)
    # moveServo(c.servoBotGuyArm, c.botGuyArmDown, 5)
    #cpp.drive_distance(-3.5, 40)


def getCrates():
    print "Picking up crates"
    #drives center area grabs cube
    p.set_second_position()
    p.set_final_positions()
    cpp.rotate(85, 20)
    cpp.drive_distance(-2, 30)
    msleep(1000)
    cpp.drive_conditional(black_left_or_right, -20, state=True)     #work on fixing alignment here
    squareUpOnBlack(30)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateGrab, 15)
    cpp.drive_distance(-6.5, 40)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)  # grab crates # end of func.2
    moveServo(c.servoCrateArm, c.crateArmMid, 10)
    msleep(500)
    cpp.drive_distance(10, 40)
    moveServo(c.servoCrateArm, c.crateArmMid+200, 2)
    squareUpOnBlack(-30)



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
    cpp.rotate(-84, 35)
    cpp.drive_distance(-15.5, 35)
    cpp.rotate(-90, 35)
    squareUpOnBlack(30)
    cpp.drive_distance(-9.5, 35)
    # Drop blocks below
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15)
    moveServo(c.servoCrateArm, c.crateArmDeStack, 15)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 15)
    cpp.drive_distance(-4, 35)
    cpp.drive_distance(12.5, 25)
    cpp.rotate(-90, 35)
    cpp.drive_distance(12, 30)
    cpp.rotate(88, 35)
    cpp.drive_distance(-9, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15)
    moveServo(c.servoCrateArm, c.crateArmUp)
    cpp.drive_distance(-4, 35)
    # driving back to center after dropping off crates
    cpp.drive_distance(18, 30)
    cpp.drive_conditional(black_left_or_right, -30, state=False)
    squareUpOnBlack(-30)
    cpp.rotate(86, 30)
    cpp.drive_conditional(cpp.get_black_left, 30, state=False)
    cpp.drive_distance(-3, 40)
    cpp.rotate(90, 30)


def goYellowSecond():
    print "Yellow is in second position"
    cpp.rotate(180, 20)
    squareUpOnBlack(15)
    cpp.drive_distance(-4, 30)
    cpp.rotate(18, 30)  #15
    cpp.drive_distance(-6, 15)
    # Deliver Blocks
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15) #deliver 1st crate
    moveServo(c.servoCrateArm, c.crateArmDeStack, 15)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 15)
    cpp.drive_distance(-4, 50)
    cpp.drive_distance(4, 50)
    cpp.rotate(-42, 30)
    cpp.drive_distance(-2, 30)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15 )  #deliver 2nd crate
    moveServo(c.servoCrateArm, c.crateArmUp)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
    cpp.drive_distance(-4, 50)
    moveServo(c.servoCrateArm, c.crateArmUp, 20)
    cpp.drive_distance(5, 30)
    cpp.rotate(30, 40)
    # drive back to the center position to then go and drop off bot guy
    cpp.drive_distance(8, 40)
    squareUpOnBlack(15)
    cpp.rotate(180, 20)




def goYellowThird():
    print "Yellow is in third position"
    # if yellow cube is in third zone (farthest from startbox)
    # lineFollowLeftFrontTilRightFrontBlack(100)
    cpp.rotate(87, 35)
    cpp.drive_distance(-15, 35)
    cpp.rotate(87, 35)
    squareUpOnBlack(15)
    cpp.drive_distance(-9, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15)#drop 1st crate
    moveServo(c.servoCrateArm, c.crateArmDeStack, 15)
    moveServo(c.servoCrateClaw, c.crateClawClosed, 15)
    moveServo(c.servoCrateArm, c.crateArmLiftCrate, 15)
    cpp.drive_distance(-4, 35)
    msleep(9000)
    cpp.drive_distance(6, 25)
    squareUpOnBlack(15)
    cpp.rotate(87, 35)
    cpp.drive_distance(9.5, 30)
    cpp.rotate(-86, 35)
    moveServo(c.servoCrateArm, c.crateArmMid, 15)
    cpp.drive_distance(-9, 35)
    moveServo(c.servoCrateArm, c.crateArmDown, 15)
    moveServo(c.servoCrateClaw, c.crateClawSlightlyOpen, 15)#drop 2nd crate
    moveServo(c.servoCrateArm, c.crateArmDeStack)   #not actually destacking, just need value to move under cog railway
    cpp.drive_distance(-4, 30)
    # driving back to the center to then go and drop off bot guy
    cpp.drive_distance(19, 30)
    cpp.drive_conditional(black_left_or_right, -30, state=False)
    squareUpOnBlack(-10)
    cpp.rotate(-86, 30)
    cpp.drive_conditional(cpp.get_black_right, 30, state=False)
    cpp.drive_distance(-3, 40)
    cpp.rotate(-86, 30)
    squareUpOnBlack(15)


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
    cpp.rotate(87, 30)
    cpp.drive_distance(20, 30)
    cpp.rotate(-86, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmHigh)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=False)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=True)
    # cpp.drive_distance(2, 30)
    cpp.rotate(30, 20)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)


def goRedSecond():  # when red is in second position drop botguy off there
    cpp.drive_distance(2, 30)
    cpp.rotate(10, 30)
    cpp.drive_distance(9, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown, 5)
    cpp.drive_distance(2, 30)


def goRedThird():  # when red is in third position drop botguy off there
    cpp.rotate(86, 30)
    wait_for_button()
    cpp.drive_distance(23, 30) #15
    cpp.rotate(90, 30)
    moveServo(c.servoBotGuyArm, c.botGuyArmUp)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=False)
    cpp.drive_conditional(cpp.get_black_front_left, 30, state=True)
    cpp.drive_distance(2, 30)
    cpp.rotate(30, 15)
    moveServo(c.servoBotGuyArm, c.botGuyArmDown)