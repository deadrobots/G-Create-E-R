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
    act.getOutOfStartBox()
    act.pickUpDateBinsExperiment()
    act.driveToSecondDateBin()
    act.driveToCenter()
    act.seeBlocks()
    act.getCrates()
    u.DEBUG()
    act.getBotGuy()
    act.driveToYellow()
    act.dropBlocks()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()