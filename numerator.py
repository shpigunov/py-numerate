#!/usr/local/bin/python3
# Create spelled figures from numerals in Python 3

from math import log
from random import randint
from sys import argv

def numerate (numeral):

    # Map digits and digit combinations to their English names
    onesMap = {
        "0" : "zero",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine"
    }
    teensMap = {
        "10" : "ten",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "15" : "fifteen",
        "16" : "sixteen",
        "17" : "seventeen",
        "18" : "eighteen",
        "19" : "nineteen",
    }

    tensMap = {
        "2" : "twenty",
        "3" : "thirty",
        "4" : "forty",
        "5" : "fifty",
        "6" : "sixty",
        "7" : "seventy",
        "8" : "eighty",
        "9" : "ninety"
    }

    groupsMap = {
        "1" : "hundred",
        "2" : "thousand",
        "3" : "million",
        "4" : "billion",
        "5" : "trillion"
    }

    # Special case: if numeral == 0 then return "zero" and return
    if numeral == 0:
        return onesMap[str(numeral)]


    # Split into groups:

    # Reverse digits for splitting into groups
    digits = str(numeral)[::-1]

    # Determine number of groups:
    if len(digits) % 3 != 0:
        numGroups = len(digits) // 3 + 1
    else:
        numGroups = len(digits) // 3

    # Distribute by groups
    groups = []
    for g in range(0, numGroups):
        groups.append(digits[0+g*3:3+g*3])

    # Reverse groups
    for i in range(0, len(groups)):
        groups[i] = groups[i][::-1]
    groups = groups[::-1]

    # Write words

    # Initialize empty string
    spelled = ""

    for i in range(0, len(groups)):

        # Initialize teens boolean to False
        teens = False

        # If a group has hundreds i.e. "100"
        if len(groups[i]) > 2:
            if groups[i][0:1] != "0":
                spelled += onesMap[groups[i][0:1]] + " " + "hundred" + " "

        # If a group has tens i.e. "010"
        if len(groups[i]) > 1:

            # Assign indices for variable group sizes
            j = len(groups[i]) - 2
            k = len(groups[i])
            l = len(groups[i]) - 1

            # Add "teens", i.e. "011" into string
            if groups[i][j:k] in teensMap:
                spelled += teensMap[groups[i][j:k]] + " "
                teens = True

            # Add "tens", i.e. "010" into string
            if groups[i][-2] in tensMap:
                spelled += tensMap[groups[i][-2]] + " "

        # Add ones, i.e. "001" into string
        if groups[i][-1] != "0" and teens != True:
            spelled += onesMap[groups[i][-1]] + " "

        # Add group name e.g. billion 3
        if groupsMap[str(numGroups - i)] != "hundred":
            if groups[i] != "000":
                spelled += groupsMap[str(numGroups - i)] + " "

    # Return string with stripping extra spaces
    return spelled.strip()

# Unix-like CLI:

# Main function
def main(argv):
    if len(argv) < 1:
        print("Please input one positive integer argument.")
    elif len(argv) == 1:
        try:
            print(numerate(argv[0]))
        except KeyError:
            print ("Error: Probably, the provided argument is not an integer.")
    else:
        print("More than one argument is not supported yet.")

if __name__ == "__main__":
   main(argv[1:])
