#!/usr/bin/python
# -*- coding: utf-8 -*-

# Assignment for week 50 by Martin Jørgensen, tzk173


import sys
import os.path
import matplotlib.pyplot as plt

def linRegrAn(d):
    """
    Udfører en lineær regressionsanalyse på et sæt af observation.
    @param d er en liste af tupler med observationer.
    """
    xsum = 0.0
    ysum = 0.0
    sak  = 0.0
    sap  = 0.0
    a    = 0.0

    # Udregn gennemsnittet af alle x'er og y'er.
    for pair in d.iteritems():
        xsum += float(pair[0])
        ysum += float(pair[1])
    xsnit = xsum/len(d)
    ysnit = ysum/len(d)

    # Udregn summen af afvigelsersnes kvadrater og produkterne.
    for pair in d.iteritems():
        sak += pow((float(pair[0]) - xsnit) ,2)
        sap += (float(pair[0]) - xsnit) * float(pair[1])
    a = sap/sak

    # Lambda funktion til at udregne den lineære regression.
    f = lambda x: a * (float(x) - xsnit) + ysnit

    # Mindste og største x værdi.
    xmin = min(d.iteritems())[0]
    xmax = max(d.iteritems())[0]

    return ([xmin, xmax], [f(xmin), f(xmax)])

def danHashtabel(filnavn):
    """
    Returnere en hashtabel ud fra indholdet af en fil.
    @param filnavn en streng med den absolutte sti til en fil med observationer.
    """
    # Se om filen eksistere.
    if not(os.path.exists(filnavn)):
        raise IOError("Filen " + filnavn + " blev ikke fundet.")

    tabel = {}

    # Forsøg at læse linjerne i filen, hvis det ikke lykkedes så
    # udskriv passende fejl og returner en tom hashtabel.
    try:
        lines = [line.strip() for line in open(filnavn)]
    except IOError:
        print "IOError: Filen " + filnavn + " kunne ikke åbnes."
        return tabel

    # Hvis der ikke var nogen linjer i filen så skriv en passende fejl
    # og returner en tom hashtabel.
    if (len(lines) < 1):
        print "Filen " + filnavn + " var tom."
        return tabel

    # Parse alle linjerne, eller smid en fejl for ugyldigt syntax.
    for line in lines:
        try:
            x = line.split(',')[0].strip()
            y = line.split(',')[1].strip()
            tabel[x] = y
        except:
            raise Exception("Filen har ugyldigt syntax, sørg for formatet 'x.xx , y.yy'")
    # Returner hashtabellen.
    return tabel

def main(args):
    """
    Main function for at tillade brug som modul og som kørtbart script.
    """
    #sti = "D:/Dropbox/4th year/Blok 2 - PoP/ugeopgaver/flueæg.txt"
    #sti2 = "D:/Dropbox/4th year/Blok 2 - PoP/ugeopgaver/pattedyr.txt"
    sti = "flueæg.txt"

    # Kode fra ugesedlen.
    plt.plot(* linRegrAn(danHashtabel(sti)))
    plt.show()
    return 0
if __name__ == '__main__':
    main(sys.argv)
