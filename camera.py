from wallaby import *
import constants as c
import actions as a
import utilities as u

def cameraInit():
    #Initializes/Opens up camera
    print("Running!")
    if camera_open_black() == 0:
        print("camera does not open")
        exit(0)
    else:
        print("camera open")
    if camera_update() == 0:
        print("no update")
    else:
        print("update")
    i=0
    while(i < 5):
        camera_update()
        i+=1
        msleep(600)


def _getCenterColorAvg():
    #Determines what color block is within the orange card
    #This uses mode of the returned colors..
    i = 0
    while (i < 5):
        camera_update()
        i += 1
        msleep(60)
    redCount = 0
    greenCount = 0
    yellowCount = 0
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        if get_object_count(c.ORANGE) > 0 and get_object_area(c.ORANGE,0) > c.ORANGE_AREA:
            # print("Found orange")
            # print(" ")
            # print("color proximity:" + str(colorProximity(c.RED)))
            # print("get obj area:" + str(get_object_area(c.RED,0)))
            # print("get obj count:" + str((get_object_count(c.RED) > 0)))

            if get_object_count(c.YELLOW) > 0 and get_object_area(c.YELLOW,0) > c.RGY_AREA and colorProximity(c.YELLOW):
                yellowCount += 1
            if (get_object_count(c.GREEN) > 0) and get_object_area(c.GREEN,0) > c.RGY_AREA and colorProximity(c.GREEN):
                greenCount += 1
            if (get_object_count(c.RED) > 0) and get_object_area(c.RED,0) > c.RGY_AREA and colorProximity(c.RED):
                redCount += 1
        else:
            print("I see approximately no orange")

    print("Colors are:")
    print(redCount)
    print(greenCount)
    print(yellowCount)
    print("what it returns is:")

    if max(redCount, greenCount, yellowCount)==0:
        return None
    elif max(redCount, greenCount, yellowCount) == greenCount:
        return c.GREEN
    elif max(redCount, greenCount, yellowCount) == redCount:
        return c.RED
    elif max(redCount, greenCount, yellowCount) == yellowCount:
        return c.YELLOW

def _readColorWithoutOrange():
    # Determines what color block is without orange card
    # This uses mode of the returned colors..
    i = 0
    while (i < 5):
        camera_update()
        i += 1
        msleep(60)
    redCount = 0
    greenCount = 0
    yellowCount = 0
    startTime = seconds()
    while (seconds() - startTime < .5):
        camera_update()
        msleep(50)
        # print(" ")
        # print("color proximity:" + str(colorProximity(c.RED)))
        # print("get obj area:" + str(get_object_area(c.RED, 0)))
        # print("get obj count:" + str((get_object_count(c.RED) > 0)))

        if get_object_count(c.YELLOW) > 0 and get_object_area(c.YELLOW, 0) > c.FIRST_RGY_AREA:
            yellowCount += 1
        if (get_object_count(c.GREEN) > 0) and get_object_area(c.GREEN, 0) > c.FIRST_RGY_AREA:
            greenCount += 1
        if (get_object_count(c.RED) > 0) and get_object_area(c.RED, 0) > c.FIRST_RGY_AREA:
            redCount += 1
    print("Colors are:")
    print(redCount)
    print(greenCount)
    print(yellowCount)
    print("what it returns is:")

    if max(redCount, greenCount, yellowCount) == 0:
        print "No color seen in first block; ending run due to inconclusive reading"
        return None
    elif max(redCount, greenCount, yellowCount) == greenCount:
        return c.GREEN
    elif max(redCount, greenCount, yellowCount) == redCount:
        return c.RED
    elif max(redCount, greenCount, yellowCount) == yellowCount:
        return c.YELLOW


def colorProximity(color):
    #Tests to see if the center of the colored block is within a certain proximity to the center of the orange card
    if abs(get_object_center_x(color, 0)- get_object_center_x(c.ORANGE,0)) < c.COLOR_PROXIMITY: # and get_object_center_y(color,0) < get_object_center_y(c.ORANGE,0):
        return True
    return False

def colorValue(color):
    #Prints data (x,y,area) of the selected color channel
    print(colorDefine(color))
    print("objects=" + str(get_object_count(color))),
    print(", x=" + str(get_object_center_x(color, 0))),
    print(", y=" + str(get_object_center_y(color, 0))),
    print(", area=" + str(get_object_area(color, 0)))


def colorDefine(color):
    #Converts channel number to color
    if color==c.ORANGE:
        return "Nothing"
    elif color==c.RED:
        return "RED"
    elif color==c.GREEN:
        return "GREEN"
    elif color==c.YELLOW:
        return "YELLOW"


def determineOrder(list):
    """
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    """
    print(list)
    options=[c.GREEN, c.RED, c.YELLOW]
    #Logic to determine which color block is in which place
    #(work in progress) If one of the first two spots checked is empty, robot drives to final scoring zone to check last color
    #Prints a list with order of colors

    for color in list:      #removes colors detected by camera
        if color in options:
            options.remove(color)

    for i in range(len(list)):      #replaces any unknown colors
        if list[i] == c.ORANGE and options:
            guess = options.pop()
            print("cannot see color, added " + str(guess))
            list[i]=guess

    if len(list) < 3:               #adds last color based off of remaining options
        last = options.pop()
        print("Added " + str(last))
        list.append(last)
    print(list)
    print("final order: " + str([colorDefine(list[0]), colorDefine(list[1]), colorDefine(list[2])]))
    # Trying to reorder the colors because create looks at the second block first and the third block second.
    # list = [list[2], list[0], list[1]]
    # print("resorted final order: " + str([colorDefine(list[0]), colorDefine(list[1]), colorDefine(list[2])]))


def checkColor(list):
    #Finds color and adds it to the list
    s = _getCenterColorAvg()
    list.append(s)
    print(list[-1])
    return list[-1]

def checkColorWithoutOrange(list):
    s = _readColorWithoutOrange()
    list.append(s)
    print(list[-1])
    return list[-1]


position = {1: None, 2: None, 3: None}
colors = {c.GREEN: 'green', c.YELLOW: 'yellow', c.RED: 'red', c.ORANGE: 'orange', None:None}


def set_first_position():
    global position
    position[1] = _readColorWithoutOrange()
    print('position one is: {}'.format(colors[position[1]]))


def set_second_position():
    global position
    position[2] = _getCenterColorAvg()
    print('position two is: {}'.format(colors[position[2]]))


def set_final_positions():
    global position
    options = [c.GREEN, c.RED, c.YELLOW]
    if position[1] in options:
        options.remove(position[1])
    else:
        position[1] = options.pop(0)
    if position[2] in options:
        options.remove(position[2])
    else:
        position[2] = options.pop(0)
    position[3] = options[0]

    print('final position one is: {}'.format(colors[position[1]]))
    print('final position two is: {}'.format(colors[position[2]]))
    print('final position three is: {}'.format(colors[position[3]]))


def get_positions():
    return position
