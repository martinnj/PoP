# -*- coding: utf-8 -*-
#!/usr/bin/python


import sys
from math import sqrt

def findRoots(a, b, c):
    """
    Calculates the roots of a polynomial.
    """
    if b <= 0:
        x1 = (-b+sqrt(b**2-4*a*c)) / (2*a)
    else:
        x1 = (-b-sqrt(b**2-4*a*c)) / (2*a)

    if x1 != 0:
        x2 = (c/a)/x1
    else:
        x2 = -b/a

    print x1
    print x2

def main(args):
    """
    Artificial main function for posterity and great import.
    """
    findRoots(1,1000.001,1)

if __name__ == '__main__':
    main(sys.argv)
