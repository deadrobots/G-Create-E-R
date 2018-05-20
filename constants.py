
from wallaby import digital


FRONT_BUMPED = 0
ALLOW_BUTTON_WAIT = True
START_TIME = 0

#Motor Ports
leftMotor = 0
rightMotor = 2
cogMotor = 3

# Drive Info
TURN_TIME = 0

LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1
IGUS_BUTTON = 9

#Analog Ports
STARTLIGHT = 0

IS_YELLOW_BOT = digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = digital(ROBOT_ID_BLUE)
IS_ORANGE_BOT = not IS_BLUE_BOT and not IS_YELLOW_BOT



if IS_ORANGE_BOT:

    servoIgus = 0
    servoClaw = 1


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
    armBotguyPickUp = 60    #-630
    armScore = 230     #-415

elif IS_BLUE_BOT:
    #Servo Ports
    servoIgus = 2
    servoClaw = 3

    INCHES_TO_TICKS = 560

    #Claw Servo Values
    clawClosed = 230
    clawMid = 550
    clawBotguy = 785
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

    #current motor arm values
    armVeryHigh = -150
    #armBotguyDelivery = -260
    armTram = -315   #-305
    armHigh = -290
    #armDelivery = -385
    armUp = -410
    armSlightlyUp = -570
    armSandwich = -595
    armBotguy = -640    #-615
    #armBotguyPickUp = -675 #-665
    armStartbox = -700

    armBotguyDelivery = 420
    armBotguyPickUp = 50  # -630
    armScore = 310

