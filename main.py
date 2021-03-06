#!/usr/bin/python
import os, sys
import actions as act
import createPlusPlus as cpp
import constants as c
from wallaby import *
import utilities as u
import movement as m
from camera import determineOrder

def main():
    act.init()
    if u.wait_for_selection(): #asks for button press twice; FIX THIS in method
        act.getOutOfStartBoxSeeding()
        act.pickUpDateBinsExperiment()
        act.driveToSecondDateBin()
        act.driveToCenterSeeding()
    else:
        act.getOutOfStartBoxAndDriveToCenter()
    act.seeBlocks()
    act.getCrates()
    act.getBotGuy()
    act.driveToYellow()
    act.dropBlocks()
    cpp.disconnect()
    exit(0)
    u.DEBUG()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()