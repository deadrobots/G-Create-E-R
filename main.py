#!/usr/bin/python
import os, sys
import actions as act
import createPlusPlus
import constants as c
from wallaby import *
import utilities as u
import movement as m
import motorz
from camera import determineOrder

def main():
    # motorz.test()
    with createPlusPlus.Create(full=False) as cpp:
        print("Running!")
        act.init(cpp)
        # act.temp_init(cpp)
        act.getOutOfStartBoxSeeding()
        act.pickUpDateBinsExperiment()
        act.driveToSecondDateBin()
        act.driveToCenterSeeding()
        act.getCrates()
        act.getBotGuy()
        act.driveToYellow()
        act.driveToRed()
        u.DEBUG()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()