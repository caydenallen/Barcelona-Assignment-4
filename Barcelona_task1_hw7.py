#!/usr/bin/env python3
import sys
from urllib.request import urlopen
import re
import csv
#		CS3030
#		File: Barcelona_task1_hw7.py
#		Author: Team Barcelona
#		Description:
#
#



def test():
    """"
    test
    """
    canOpen = 0
    rOpen = 0
    lOpen = 0
    gsPark = 0
    pattern = re.compile("/[PpNnDd123rR]/g")

    if GS == "p" | GS == "P":
        gsPark = 1
        canOpen = 1
    elif pattern.match(GS) and len(GS) == 1:
        gsPark = 0
        canOpen = 0
    else:
        gsPark = 2
        canOpen = 0

    if canOpen == 1 & ML == 1:
        if (LI == 1 & CL == 0) | LD == 1 | LD == 1:
            lOpen = 1
        else:
            lOpen = 0
        
        if (R1 == 1 & CL == 0) | RD == 1 | RD == 1:
            rOpen = 1
        else:
            rOpen = 0

    else:
        lOpen = 0
        rOpen = 0


    doorText = ""
    if canOpen == 0 | (lOpen == 0 & rOpen == 0):
        if gsPark == 2:
            doorText = "Invalid Record: "
        doorText = doorText + "Both doors stay closed."
    elif lOpen == 1 &rOpen ==1:
        doorText = "Both doors open."
    else:
        if lOpen == 1:
            doorText = "Left door opens."
        else:
            doorText = "Right door opens."

    return doorText




def defaultFunction():
    """
    Help Comment
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as data:
        #csv_data = csv.reader(data)
        for row in data:
            print(row)
            print("Reading Record", row[0])
            print("Left dashboard switch (0 or 1): ", row[1])
            print("Right dashboard switch (0 or 1): ", row[2])
            print("Child lock switch (0 or 1): ", row[3])
            print("Master unlock switch (0 or 1): ", row[4])
            print("Left inside handle (0 or 1): ", row[5])
            print("Left outside handle (0 or 1): ", row[6])
            print("Right inside handle (0 or 1): ", row[7])
            print("Right outside handle (0 or 1): ", row[8])
            print("Gear shift position (P,N,D,1,2,3, or R)", row[9])

        print(test())
            

#Main Function
def main():
    """
    Main Function
    """
    defaultFunction()


if __name__ == "__main__":
    main()

