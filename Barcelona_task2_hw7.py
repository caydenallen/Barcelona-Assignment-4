#!/usr/bin/env python3
import sys
from urllib.request import urlopen

#		CS3030
#		File: Barcelona_task2_hw7.py
#		Author: Team Barcelona
#		Description: Will ask for Zipcodes, once you are done
#                   Will run a test script to test barcodes
#



def usage():
    """
    Usage Function
    """
    print("Usage", sys.argv[0])
    exit(0)

def printBarCode(z):
    """
    Takes in an Array of Zipcode and Prints the Barcode
    """
    zipCode = []
    for i in range(5):
        zipCode.append(z[i])
    r = "|"
    s = 0
    for i in zipCode:
        s += int(i)
    checkDigit = 0
    while ((s%10) != 0):
        s = s + 1
        checkDigit = checkDigit + 1
    zipCode.append(str(checkDigit))

    for i in zipCode :
        if (i == "1") :  r += ":::||"
        elif(i == "2") : r += "::|:|"
        elif(i == "3") : r += "::||:"
        elif(i == "4") : r += ":|::|"
        elif(i == "5") : r += ":|:|:"
        elif(i == "6") : r += ":||::"
        elif(i == "7") : r += "|:::|"       
        elif(i == "8") : r += "|::|:"
        elif(i == "9") : r += "|:|::"
        elif(i == "0") : r += "||:::"
    r += "|"
    print(r)

def printDigit(z):
    """
    Takes in a Zipcode and prints the Digit based on the weight 7, 4, 2, 1, 0
    """
    Digit = 0
    Digit += z[0] * 7
    Digit += z[1] * 4
    Digit += z[2] * 2
    Digit += z[3] * 1
    Digit += z[4] * 0
    print(Digit)


def testModule():
    """
    Calls Web API to test the zip to barcode
    """
    urlfile = urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt")
    for lines in urlfile:
        errortemp = []
        errorlines = lines.split()
        for logs in errorlines:
            errortemp.append(logs.decode("utf-8"))
        printBarCode(errortemp[0])

        

#Main Function
def main(argv):
    """
    Main Function
    """
    if (len(sys.argv) > 1):
        usage()
    again = "y"
    while(again == "y"):
        zipCode = input("Enter a Zipcode (xxxxx) q to quit:")
        if (zipCode == "q"):
            exit(0)
        zipCode = zipCode.rstrip()
        try:
            z = int(zipCode)
        except ValueError:
            print("Error: Zip code is not all numeric")
        else:
            if(len(zipCode) != 5):
                print("Error: Zip code is not 5 digits")
            else:
                printBarCode(zipCode)        

        again = input("Enter another Zipcode? (y/n)")
    
    testModule()

if __name__ == "__main__":
    main(sys.argv)
    exit(0)

