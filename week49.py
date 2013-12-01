#!/usr/bin/python
# -*- coding: utf-8 -*-

# Assignment for week 49 by Martin Jørgensen, tzk173


import sys

def same_len(xrr):
    """
    Checks if all the lists in a list of lists have the same length.
    @params xrr a list of lists to check.
    @return True if all lists in xrr are the same length, false otherwise.
    """
    xrrlen = len(xrr)
    if (xrrlen == 0):
        return False
    elif (xrrlen == 1):
        return True
    else:
        tgtlen = len(xrr[0])
        for xr in xrr:
            if (len(xr) != tgtlen):
                return False
        return True


def unique_members(xrr):
    """
    Generate a list of unique members in the inner lists of a list of lists.
    @param xrr a list of lists to generate members from.
    @return A list of all unique members.
    """
    members = []
    for xr in xrr:
        for x in xr:
            if x not in members:
                members.append(x)
    return members

def mooo(x,y,xrr):
    """
    Check if x and y Meets Once and Only Once in the list of lists.
    This method name is not as generic as the work it actually does, but
    I could not resists the temptation to call a method for "mooo" :)
    @param x the first element to check.
    @param y the second element to check.
    @param xrr the list of lists to check for elements in.
    @return True if x and y meets exactly once, false otherwise.
    """
    collisions = 0
    for xr in xrr:
        if (x in xr) and (y in xr):
            collisions += 1
    return (collisions == 1)

def is_BS(xrr):
    """
    Checks a list of lists if it represents a block system.
    @param xrr a list of lists to check.
    @return True if xrr is a block system, false otherwise or if xrr is empty.
    """
    if (len(xrr) == 0):
        return False
    if (not same_len(xrr)):
        return False

    members = unique_members(xrr)

    for x in members:
        for y in members:
            if (x == y):
                break
            if not mooo(x,y,xrr):
                return False

    return True;

def main(args):
    """
    Artificial main function for posterity and great import.
    """

    # A valid test set.
    B1 = [['A','B','C','D'], ['A','E','I','M'], ['A','F','K','P'], ['A','G','L','N'], ['A','H','J','O'],
          ['E','F','G','H'], ['B','F','J','N'], ['B','E','L','O'], ['B','H','K','M'], ['B','G','I','P'],
          ['I','J','K','L'], ['C','G','K','O'], ['C','H','I','N'], ['C','E','J','P'], ['C','F','L','M'],
          ['M','N','O','P'], ['D','H','L','P'], ['D','G','J','M'], ['D','F','I','O'], ['D','E','K','N']]

    # An invalid test set. (B meets itself)
    B2 = [['B','B','C','D'], ['A','E','I','M'], ['A','F','K','P'], ['A','G','L','N'], ['A','H','J','O'],
          ['E','F','G','H'], ['B','F','J','N'], ['B','E','L','O'], ['B','H','K','M'], ['B','G','I','P'],
          ['I','J','K','L'], ['C','G','K','O'], ['C','H','I','N'], ['C','E','J','P'], ['C','F','L','M'],
          ['M','N','O','P'], ['D','H','L','P'], ['D','G','J','M'], ['D','F','I','O'], ['D','E','K','N']]
    # An invalid test set. (Inner list lengths are not the same)
    B3 = [['A','B','C','D'], ['A','E','I','M'], ['A','F','K','P'], ['A','G','L','N'], ['A','H','J','O'],
          ['E','F','G','H'], ['B','F','J','N'], ['B','E','L','O'], ['B','H','K','M'], ['B','G','I','P'],
          ['I','J','K','L'], ['C','G','K','O'], ['C','H','I','N'], ['C','E','J','P'], ['C','F','L','M'],
          ['M','N','O','P'], ['D','H','L','P'], ['D','G','J','M'], ['D','F','I','O'], ['D','E','K']]
    # An invalid test set. (R does not meet everyone)
    B4 = [['R','B','C','D'], ['A','E','I','M'], ['A','F','K','P'], ['A','G','L','N'], ['A','H','J','O'],
          ['E','F','G','H'], ['B','F','J','N'], ['B','E','L','O'], ['B','H','K','M'], ['B','G','I','P'],
          ['I','J','K','L'], ['C','G','K','O'], ['C','H','I','N'], ['C','E','J','P'], ['C','F','L','M'],
          ['M','N','O','P'], ['D','H','L','P'], ['D','G','J','M'], ['D','F','I','O'], ['D','E','K','N']]

    print "Expectation / Result"
    print "===================="
    print "True  / " + str(is_BS(B1)) # True
    print "False / " + str(is_BS(B2)) # False
    print "False / " + str(is_BS(B2)) # False
    print "False / " + str(is_BS(B2)) # False

    return 0
if __name__ == '__main__':
    main(sys.argv)
