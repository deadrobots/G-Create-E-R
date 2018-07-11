
from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

#camera channels
ORANGE = 0
RED = 1
GREEN = 2
YELLOW = 3

clawMotor = 0

# Servo Ports
servoCrateClaw = 0
servoBotGuyArm = 1
servoCrateArm = 2
servoBotGuyClaw = 3

# Drive Info
TURN_TIME = 0

LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1
ROBOT_ID_GREEN = 2

#Analog Ports
STARTLIGHT = 0
FRONT_TOPHAT = 5

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_GREEN_BOT = digital(ROBOT_ID_GREEN)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT and not IS_GREEN_BOT

FIRST_RGY_AREA = 40

if IS_BLUE_BOT:

    INCHES_TO_TICKS = 560

    # Botguy Arm Servo Values
    botGuyArmUp = 1400
    botGuyArmMid = 600
    botGuyArmDown = 500
    botGuyArmStart = 1570

    # Crate arm servo values
    crateArmDown = 830
    crateArmAlmostDown = 962
    crateArmMid = 1000
    crateArmStart= 1000
    crateArmDeStack = 1200
    crateArmLiftCrate = 1500
    crateArmUp = 1600  # 1400

    # Crate claw servo values
    crateClawClosed = 200 #380
    crateGrab = 900
    crateClawOpen = 1200  #1060
    crateClawStart = 1250

    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60

    # not used
    crateArmVeryHigh = 2000
    crateArmCarry = 1200
    crateClawSlightlyOpen = 760

elif IS_GREEN_BOT:

    INCHES_TO_TICKS = 560
    # Botguy claw is now motor
    clawBotguy = 500

    # Botguy Arm Servo Values
    botGuyArmUp = 700
    botGuyArmMid = 800
    botGuyArmDown = 1075
    botGuyArmStart = 0

    # CrateArm Servo Values
    crateArmDown = 880
    crateArmAlmostDown = 950
    crateArmMid = 1050
    crateArmStart = 1800
    crateArmDeStack = 1300
    crateArmLiftCrate = 1500
    crateArmUp = 2047

    #Crate Claw Servo Values
    crateClawClosed = 200 #500
    crateGrab = 750
    crateClawOpen = 1650
    crateClawStart = 1800

    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60