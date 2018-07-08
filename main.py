#!/usr/bin/python
import os, sys
import actions as act
import createPlusPlus
import constants as c
from wallaby import *
import utilities as u
import movement as m
from camera import determineOrder

def main():
    with createPlusPlus.Create() as cpp:
        act.init(cpp)
        act.centerPipeRunAndBotGuyGrab()
        act.headToSecondBlock()
        act.getCrates()
        act.driveToYellow()
        #act.dropBlocks()
        # cpp.disconnect()
        # exit(0)




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()