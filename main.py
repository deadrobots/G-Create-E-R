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
    # act.pickUpDateBinsExperiment()
    # u.DEBUG()
    act.getOutOfstartBox()
    act.getCrates()
    u.DEBUG()
    act.getBotGuy()
    act.gotoSecondBlock()
    act.seeBlocks2()
    act.goToBlock3()
    act.seeBlocks3()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()