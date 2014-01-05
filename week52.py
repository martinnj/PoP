#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Ugeopgave for uge 52 af Martin Jørgensen og Sarah Vang Nøhr.

import sys

class simplematrix:
    """
    Simpel matrice klasee som indeholder grunlæggende lineær algebra
    funktioner.
    """
    _values = [[]]
    def __init__():
        """
        """
    def __init__(m, n):
        """
        """
    def __init__(m, n, values):
        """
        """
    def __str__():
        """
        """
    def read(sti):
        """
        """
    def write(sti):
        """
        """
    def __add__(A, B):
        """
        """
    def __mul__(A, B):
        """
        """
    def __cmp__(A, B):
        """
        """
    def __eq__(A, B):
        """
        """


def main(args):
    """
    Main function for at tillade brug som modul og som kørtbart script.
    """
    print "Nu afprøves matrixaddition for tilfælde 2 lige store matricer"
    A = simplematrix(2 ,2, [1,2,3,4])
    B = simplematrix(2, 2, [5,6,7,8])
    C = simplematrix(2, 2, [6,8,10,12])
    print C == A + B

    return 0

if __name__ == '__main__':
    main(sys.argv)
