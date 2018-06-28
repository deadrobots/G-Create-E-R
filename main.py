#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utilities as u
import movement as m
from camera import determineOrder

def main():
    print("Running!")
    act.init()
    act.getOutOfStartBoxAndDriveToCenter()
    # act.getOutOfStartBoxSeeding()
    # act.pickUpDateBinsExperiment()
    # act.driveToSecondDateBin()
    # act.driveToCenterSeeding()
    act.seeBlocks()
    act.getCrates()
    act.getBotGuy()
    act.driveToYellow()
    act.dropBlocks()
    u.DEBUG()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()