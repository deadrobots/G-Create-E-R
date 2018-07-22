#!/usr/bin/python
import os, sys
import actions as act
import createPlusPlus
import constants as c
from wallaby import *
import utilities as u
import movement as m
from camera import determineOrder
import Shutdown

def main():
    with createPlusPlus.Create(full=True) as cpp:
        act.init(cpp)
        Shutdown.die_after_time(main_two, 118)


def main_two():
    act.centerPipeRunAndBotGuyGrab()
    act.headToSecondBlock()
    act.getCrates()
    act.driveToYellow()
    act.driveToRed()
    u.DEBUG()
    # cpp.disconnect()
    # exit(0)




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()