#!/usr/bin/python
# -*- coding: utf-8 -*-

# Assignment for week 48 by Martin Jørgensen, tzk173


import sys
from math import sqrt, floor

def convrgntsReal(x, n):
    """
    Takes a float x and a non-negative integer n and prints the
    convergents through the chained-fractions.
    """

    # Make sure the arguments are of proper nature.
    # The assignment specified float as type of x, so I enforced
    # it even though an int should work as well.
    if (type(x) != float) or (n < 0):
        print "Bad parameters."
        return

    # Initialize the A/B values and x.
    a0 = 0
    a1 = 1
    b0 = 1
    b1 = 0
    lastx = x

    # Begin the loop calculating the fractions
    for i in range(0,n):
        lastq = int(floor(lastx))
        a2 = (lastq * a1 + a0)
        b2 = (lastq * b1 + b0)

        # Naive zero-division guard.
        if b2 != 0:
            k = a2/b2
        else:
            print "Division by zero!"
            return
        # K is satisfying, lets quit :)
        if k == x:
            return
        
        # Print the fraction.
        print str(a2) + "/" + str(b2)

        # Naive zero-division guard.
        if (lastx - lastq) == 0:
            print "Division by zero!"
            return
        # Prepare values for next iteration.
        lastx = 1 / (lastx - lastq)
        a0 = a1
        a1 = a2
        b0 = b1
        b1 = b2
        

def main(args):
    """
    Artificial main function for posterity and great import.
    """
    convrgntsReal(sqrt(2), 6)  # Example from assignment.
    convrgntsReal(-1.1, 19)    # Division by zero.
    convrgntsReal(4.52, 15)    # Goes on to biiig numbers.
    convrgntsReal(sqrt(2), -1) # Bad parameters. (n is negative)

if __name__ == '__main__':
    main(sys.argv)
