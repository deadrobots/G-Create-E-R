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
    act.centerPipeRun()
    act.headToSecondBlock()
    act.getCrates()
    u.DEBUG()
    # act.getBotGuy()
    # act.driveToYellow()
    # act.dropBlocks()
    # cpp.disconnect()
    # exit(0)




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()