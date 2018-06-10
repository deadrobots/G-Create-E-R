
from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

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

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_GREEN_BOT = digital(ROBOT_ID_GREEN)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT and not IS_GREEN_BOT

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

    armBotguyDelivery = 400
    armBotguyPickUp = 450    #-630
    armScore = 230     #-415

elif IS_BLUE_BOT:

    INCHES_TO_TICKS = 560

    #Claw Servo Values
    clawClosed = 0
    clawMid = 550
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

    crateArmUp = 560
    crateArmCarry = 1100
    crateArmDown = 1820
    crateArmStart= 1000
    crateArmMid = 800

    botGuyArmUp = 1400
    botGuyArmDown = 500
    botGuyArmStart = 1570

    crateClawClosed = 350 #380
    crateClawOpen = 1060
    crateClawStart = 1250


    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60

elif IS_GREEN_BOT:

    INCHES_TO_TICKS = 560

    # Claw Servo Values
    clawClosed = 450
    clawLoose = 1000
    clawBotguy = 830
    clawbotguyArea = 1050
    clawMid = 1200
    clawOpen = 1850
    clawStart = 2047


    # Botguy Arm Servo Values
    botGuyArmUp = 1400
    botGuyArmDown = 500

    # Crate Arm Servo Values
    crateArmUp = 1400
    crateArmMid = 200
    crateArmDown = 50

    #Crate Claw Servo Values
    crateClawClosed = 825
    crateClawOpen = 1700

    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 60