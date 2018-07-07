
from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

#camera channels
ORANGE = 0
RED = 1
GREEN = 2
YELLOW = 3

#Motor Ports
leftMotor = 0
rightMotor = 2
cogMotor = 3

# Servo Ports
servoCrateClaw = 0
servoCrateArm = 2
servoBotGuyClaw = 3
servoBotGuyArm = 1

# Drive Info
TURN_TIME = 0

LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1
ROBOT_ID_GREEN = 2
IGUS_BUTTON = 9

#Analog Ports
STARTLIGHT = 0
FRONT_TOPHAT = 5

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_GREEN_BOT = digital(ROBOT_ID_GREEN)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT and not IS_GREEN_BOT

FIRST_RGY_AREA = 40

if IS_ORANGE_BOT:

    INCHES_TO_TICKS = 600

    #Claw Servo Values
    clawClosed = 0
    clawFrisbeeTight = 397
    clawMid = 517
    clawBotguy = 620  #630
    clawTram = 917 #Position to move tram
    clawOpen = 1382
    clawStart = 2047 #All the way back; used to be 1730

    #Cog Servo Values
    cogLiftContinued = 770
    cogServoVeryHigh = 920
    evenMoreCogLift = 980
    cogLift = 1090
    cogRingDrop = 1100
    cogStartBox = 1200
    cogPegTwo = 1350
    cogStart = 1650
    cogGrab = 1725

    #current motor arm values
    armVeryHigh = -150
    armHigh = -290
    armTram = -310 #was 300
    armUp = -440
    armBotguy = -590
    armSlightlyUp = -600
    armSandwich = -620
    armStartbox = -700

    # armBotguyDelivery = 400
    # armBotguyPickUp = 850    #-630
    # armScore = 230     #-415
    # armBotguyUp = 0

elif IS_BLUE_BOT:

    INCHES_TO_TICKS = 560

    #Claw Servo Values
    clawClosed = 0
    clawMid = 600
    clawBotguy = 430#785
    clawbotguyArea = 650
    clawTram = 900  # Position to move tram
    clawOpen = 1400
    clawStart = 2047 #All the way back

    #Cog Servo Values
    cogServoVeryHigh = 15
    evenMoreCogLift = 150
    cogLift = 225
    cogRingDrop = 215
    cogStartBox = 350
    cogPegTwo = 500
    cogStart = 800
    cogGrab = 800

    crateArmUp = 1600  #1400
    crateArmMid = 1000
    crateArmDeStack = 1200
    crateArmCarry = 1200
    crateArmDown = 830
    crateArmAlmostDown = 962
    crateArmLiftCrate = 1500
    crateArmStart= 1000
    crateArmVeryHigh = 2000

    botGuyArmUp = 1400
    botGuyArmMid = 600
    botGuyArmDown = 500
    botGuyArmStart = 1570

    crateClawClosed = 200 #380
    crateGrab = 900
    crateClawOpen = 1200  #1060
    crateClawStart = 1250
    crateClawSlightlyOpen = 760

    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60

elif IS_GREEN_BOT:

    INCHES_TO_TICKS = 560

    # Claw Servo Values
    clawClosed = 0
    clawLoose = 1000
    clawBotguy = 700
    clawbotguyArea = 1150
    clawMid = 1200
    clawOpen = 1850
    clawStart = 2047


    # Botguy Arm Servo Values
    botGuyArmUp = 600
    botGuyArmMid = 800
    botGuyArmDown = 1075
    botGuyArmStart = 0

    # Crate Arm Servo Values
    crateArmUp = 2047
    crateArmMid = 1050
    crateArmDown = 880
    crateArmAlmostDown = 950
    crateArmDeStack = 1300
    crateArmLiftCrate = 1500
    crateArmStart = 1800

    #Crate Claw Servo Values
    crateClawClosed = 200 #500
    crateGrab = 800
    crateClawOpen = 1650
    crateClawStart = 1800


    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60