#!/usr/local/bin/python3

from sys import argv
import numerate

# Unix-like CLI:

# Main function
def main(argv):
    # Attempt to parse arguments
    if len(argv) < 1:
        print("Please input one positive integer argument.")
    elif len(argv) == 1:
        try:
            print(numerate.numerate(argv[0]))
        except KeyError:
            print ("Error: Probably, the provided argument is not an integer.")
    else:
        print("More than one argument is not supported yet.")

if __name__ == "__main__":
   main(argv[1:])
