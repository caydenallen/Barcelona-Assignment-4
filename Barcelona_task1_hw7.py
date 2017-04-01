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



def test(i):
    """"
    test
    """
    canOpen = 0
    rOpen = 0
    lOpen = 0
    gsPark = 0
    pattern = [' P', ' N', ' D', ' 1', ' 2', ' 3', ' R']
    #determin gear shift
    #print(i) 
    LD = (str(i[1]))
    RD = (str(i[2]))
    CL = (str(i[3]))
    ML = (str(i[4]))
    LI = (str(i[5]))
    LO = (str(i[6]))
    RI = (str(i[7]))
    RO = (str(i[8]))
    GS = (str(i[9]))
  
    #print(ML, type(ML))
    #print(RI, type(RI))



  #  temp[9] == "p"
    

    if GS == " P":
        gsPark = 1
        canOpen = 1
    elif GS.upper() in pattern:
        gsPark = 0
        canOpen = 0
    else:
        gsPark = 2
        canOpen = 0
    if canOpen == 1 and int(ML) == 1:
        # test if left door can be opened
        if (int(LI) == 1 and int(CL) == 0) or int(LO) == 1 or int(LD) == 1:
            lOpen = 1
        else:
            lOpen = 0
        # test if right door can be opened
        if (int(RI) == 1 and int(CL) == 0) or int(RO) == 1 or int(RD) == 1:
            rOpen = 1
        else:
            rOpen = 0

    else:
        lOpen = 0
        rOpen = 0


    doorText = ""
    if canOpen == 0 or (lOpen == 0 and rOpen == 0):
        if gsPark == 2:
            doorText = "Invalid Record: "
        doorText = doorText + "Both doors stay closed."
    elif lOpen == 1 and rOpen ==1:
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
    count = 0
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as data:
        temp = []

        for lines in data:
            lines = lines[:-1]
                    #logs = logs[:-1]
            temp.append(lines.decode("utf-8").split(','))
        del temp[0]            
            #print(temp)
            
            #print(templines)

        #csv_data = csv.reader(data)
            #for row in temp:i
           # print(temp)
            #print(temp) 

            #if temp[0] != "H1,":
        for i in temp:            
            count = count + 1
            print("Reading Record", count)
            print("Left dashboard switch (0 or 1): ", i[1])
            print("Right dashboard switch (0 or 1): ", i[2])
            print("Child lock switch (0 or 1): ", i[3])
            print("Master unlock switch (0 or 1): ", i[4])
            print("Left inside handle (0 or 1): ", i[5])
            print("Left outside handle (0 or 1): ", i[6])
            print("Right inside handle (0 or 1): ", i[7])
            print("Right outside handle (0 or 1): ", i[8])
            print("Gear shift position (P,N,D,1,2,3, or R)", i[9])
            print(test(i))
            print("") 

#Main Function
def main():
    """
    Main Function
    """
    defaultFunction()


if __name__ == "__main__":
    main()

