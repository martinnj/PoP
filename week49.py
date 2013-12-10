#!/usr/bin/python
# -*- coding: utf-8 -*-

# Assignment for week 49 by Martin Jørgensen, tzk173


import sys         # For the main function
import collections # For the typecheck

def same_len(xrr):
    """
    Checks if all the lists in a list of lists have the same length.
    @params xrr a list of lists to check.
    @return True if all lists in xrr are the same length, false otherwise.
    """
    xrrlen = len(xrr)

    # If xrr is empty, there is nothing to compare, assume it's wrong.
    if (xrrlen == 0):
        return False

    # If xrr has one element, it's bound to be it's own length, funnily enough.
    if (xrrlen == 1):
        return True
    else:
        # Take a sample length (the first element is a god start.
        tgtlen = len(xrr[0])

        # Check if all other elements have same length, else return false.
        for xr in xrr:
            if (len(xr) != tgtlen):
                return False

        # Success we have elements and they have the same length.
        return True


def unique_members(xrr):
    """
    Generate a list of unique members in the inner lists of a list of lists.
    @param xrr a list of lists to generate members from.
    @return A list of all unique members.
    """
    members = []
    # Go over all inner lists.
    for xr in xrr:
        # Go over all members of the inner list we're working on.
        for x in xr:
            # Check if the member of the inner list is unique.
            if x not in members:
                # If it is, add to return list, else continue.
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
    # For all the inner lists
    for xr in xrr:
        # If x and y meet in the inner list, increase counter.
        if (x in xr) and (y in xr) and (x != y):
            collisions += 1
        # If x or y is more than once in each list return false.
        if (xr.count(x) > 1) or (xr.count(y) > 1):
            return False
    # If the counter is >0 they met more than once.
    # If the counter is  0 they never met.
    # If the counter is  1 they met only once.
    return (collisions == 1)

def is_BS(xrr):
    """
    Checks a list of lists if it represents a block system.
    @param xrr a list of lists to check.
    @return True if xrr is a block system, false otherwise or if xrr is empty.
    """
    # Tyoe check, is xrr a collection?
    if ((not isinstance(xrr, collections.Iterable))
          or isinstance(xrr,basestring)):
        return False

    # Does xrr have any elements?
    if (len(xrr) == 0):
        return False

    # Are these elements proper collections?
    for xr in xrr:
        if ((not isinstance(xr, collections.Iterable))
              or isinstance(xrr,basestring)):
            print xr
            return False

    # Check if all inner lists are the same length. (1st criteria)
    if (not same_len(xrr)):
        return False

    # Generate a list of all unique members,
    # (contestants in the speedway metaphore)
    members = unique_members(xrr)

    # Go over all members and compare them to all other members
    # to make sure they meet once and only once.
    for x in members:
        for y in members:

            # Make sure we don't try to match a member with itself.
            if (x != y):
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

    # An invalid test set. (B meets itself, A does not meet all)
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
    # A valid test set. (Value datatypes should not make a difference)
    B5 = [[1,'A'], [1,0.0], ['A',0.0]]
    # An invalid test set. (This is not the correct list of lists type)
    B6 = []
    # An arguably valid test set. (The inner list live up to both BS criteria)
    B7 = [[]]
    # An invalid test set. (Does not live up to second BS criteria)
    B8 = [[1],[2]]
    # An invalid test set. (This is not the correct list of lists type)
    B9 = 'A'
    # An invalid test set. (This is not the correct list of lists type)
    B10 = 'Alice+Bob'
    # A valid test set. (Checking if lists of strings gets parsed correctly)
    B11 = ["he","ej","hj"]
    # An invalid test set. (they all meet themselves)
    B12 = [[0,1], [0,2], [1,2], [0,0], [1,1], [2,2]] 

    # Print the results of the tests.
    print "Test ##: Facit / Result"
    print "===================="
    print "Test 01: True  / " + str(is_BS(B1))
    print "Test 02: False / " + str(is_BS(B2))
    print "Test 03: False / " + str(is_BS(B3))
    print "Test 04: False / " + str(is_BS(B4))
    print "Test 05: True  / " + str(is_BS(B5))
    print "Test 06: False / " + str(is_BS(B6))
    print "Test 07: True  / " + str(is_BS(B7))
    print "Test 08: False / " + str(is_BS(B8))
    print "Test 09: False / " + str(is_BS(B9))
    print "Test 10: False / " + str(is_BS(B10))
    print "Test 11: True  / " + str(is_BS(B11))
    print "Test 12: False / " + str(is_BS(B12))

    return 0
if __name__ == '__main__':
    main(sys.argv)
