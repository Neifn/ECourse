#!/usr/bin/env python

import math
import sys


"""
 Main function calls for LocateFibonacci function and performs checks
"""
def main():

    # Cheks if number of arguments is equal to one
    if (len(sys.argv) != 2):
        print("function allows only one integer argument")
        sys.exit(1)

    # Cheks if argument's value is integer
    try:
        Number = int(sys.argv[1])

        # Cheks if argument's value is positive
        if Number < 0:
            print("Enter positive value")
            sys.exit(1)  
    except ValueError:
        print("Enter integer")
        sys.exit(1)

    # Prints value calculated by LocateFibonacci function
    print(LocateFibonacci(Number))


"""
 Function that calculates Fibonacci number
 :param Number taken from user input
"""
def LocateFibonacci(Number):

    # Performs calculations if number isn't too large 
    try: 
        Fib = int((1 / math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2) ** Number) - (((1 - math.sqrt(5)) / 2) ** Number)))
        return Fib
    except OverflowError:
        return "the value is too large"


(__name__ == '__main__') and main()
