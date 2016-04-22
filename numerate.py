#!/usr/local/bin/python3
# Create spelled figures from numerals in Python 3

from math import log
from random import randint
from csv import reader

class LanguageResources(object):
    """Container for language resources such as maps and replacement tables"""
    def __init__(self, lang):
        self.lang = lang

        # Define a list of resources we want to fetch
        resourcesList = ["replacementTable", "onesMap", "teensMap", "tensMap", "groupsMap"]

        for resource in resourcesList:
            # Init an empty dictonary for the resource
            exec("self."+resource+"={}")

            # Open a file with current resource
            try:
                f = open("./langres/{0}/{1}.csv".format(lang, resource), mode = "r")
            except FileNotFoundError:
                print("This language is not supported yet. Defaulting to English.")
                lang = "en"
                f = open("./langres/{0}/{1}.csv".format(lang, resource), mode = "r")

            # Cycle through the parsed csv file to populate current resources
            for item in reader(f.readlines()):
                # Handle empty replacement table
                try:
                    exec("self."+resource+"[item[0]] = item[1].strip()")
                except IndexError:
                    #exec("self."+resource+"['nA'] = 'nA'")
                    pass

            # File hygiene
            f.close()

            #eval("print(self."+resource+")")


def numerate (numeral, lang):

    lr = LanguageResources(lang)

    # Special case: if numeral == 0 then return "zero" and return
    if numeral == 0:
        return lr.onesMap[str(numeral)]

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
                spelled += lr.onesMap[groups[i][0:1]] + " " + lr.groupsMap["1"] + " "

        # If a group has tens i.e. "010"
        if len(groups[i]) > 1:

            # Assign indices for variable group sizes
            j = len(groups[i]) - 2
            k = len(groups[i])
            l = len(groups[i]) - 1

            # Add "teens", i.e. "011" into string
            if groups[i][j:k] in lr.teensMap:
                spelled += lr.teensMap[groups[i][j:k]] + " "
                teens = True

            # Add "tens", i.e. "010" into string
            if groups[i][-2] in lr.tensMap:
                spelled += lr.tensMap[groups[i][-2]] + " "

        # Add ones, i.e. "001" into string
        if groups[i][-1] != "0" and teens != True:
            spelled += lr.onesMap[groups[i][-1]] + " "

        # Add group name e.g. billion 3
        if lr.groupsMap[str(numGroups - i)] != lr.groupsMap["1"]:
            if groups[i] != "000":
                spelled += lr.groupsMap[str(numGroups - i)] + " "

    # Return the final string after post-processing
    return postProcess(spelled.strip(), lr)


def postProcess(string, lr):
    """Language-specific post-processing to avoid changing general logic"""

    # Replace irregularities using replacement table
    for i in list(lr.replacementTable.keys()):
        string = string.replace(i, lr.replacementTable[i])

    return string
