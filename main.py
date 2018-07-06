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
    print("Running!")
    act.init()
    if u.wait_for_selection():  # asks for button press
        print("0") # seeding (aka left)
        act.getOutOfStartBoxSeeding()
        act.pickUpDateBinsExperiment()
        act.driveToSecondDateBin()
        act.driveToCenterSeeding()
    else:
        act.getOutOfStartBoxAndDriveToCenter()
    # act.seeBlocks()
    act.getCrates()
    act.getBotGuy()
    u.DEBUG()
    act.driveToYellow()
    act.dropBlocks()
    u.DEBUG()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()