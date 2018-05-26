#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from wallaby import *
import utilities as u
import movement as m

def main():
    print("Running!")
    act.init()
    act.driveToBotguy()
    # act.driveAndSquareUp()
    #act.driveToBotguy()





if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()