
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

INCHES_TO_TICKS = 560

motorMid = 480 #570 # how wide the claw opens of the botguy grabber

#Claw Servo Values
clawClosed = 0
clawMid = 800
clawBin = 430 #785
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

crateArmUp = 1450  #1400
crateArmMid = 1200
crateArmDeStack = 1400
crateArmCarry = 1300
crateArmDown = 1175  #830
crateArmAlmostDown = 962
crateArmLiftCrate = 1600
crateArmStart= 1000
crateArmVeryHigh = 2000
crateArmGrab = 1200

botGuyArmUp = 1400
botGuyArmMid = 600
botGuyArmDown = 470
botGuyArmStart = 1570

crateClawClosed = 300 #380
crateGrab = 700  #550
crateClawOpen = 1200  #1060
crateClawStart = 1100  #1250
crateClawSlightlyOpen = 750

COLOR_PROXIMITY = 20
ORANGE_AREA = 500
RGY_AREA = 60
