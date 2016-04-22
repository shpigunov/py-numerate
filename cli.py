#!/usr/local/bin/python3

from sys import argv
import numerate

# Unix-like CLI:

# Main function
def main(argv):
    # Attempt to parse arguments
    if len(argv) < 1:
        print("Please input at least one positive integer argument.")
    elif len(argv) == 1:
        try:
            print(numerate.numerate(argv[0], "en"))
        except KeyError:
            print ("Error: Probably, the provided argument is not an integer.")
    elif len(argv) == 2:
        try:
            print(numerate.numerate(argv[1], argv[0]))
        except KeyError:
            print ("Error: Probably, the provided argument is not an integer.")
    else:
        print("Too many arguments.")

if __name__ == "__main__":
   main(argv[1:])
