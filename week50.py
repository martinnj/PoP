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
    xsum = sum(map(lambda x: float(x[0]), d.iteritems()))
    ysum = sum(map(lambda x: float(x[1]), d.iteritems()))
    xsnit = xsum/len(d)
    ysnit = ysum/len(d)

    # Udregn summen af afvigelsersnes kvadrater og produkterne.
    f = lambda x: pow((float(x[0]) - xsnit) ,2)
    g = lambda x: (float(x[0]) - xsnit) * float(x[1])
    sak = sum(map(f,d.iteritems()))
    sap = sum(map(g,d.iteritems()))
    a = sap/sak

    # Lambda funktion til at udregne den lineære regression.
    h = lambda x: a * (float(x) - xsnit) + ysnit

    # Mindste og største x værdi.
    xmin = min(map(lambda x: float(x) ,d.keys()))
    xmax = max(map(lambda x: float(x) ,d.keys()))

    return ([xmin, xmax], [h(xmin), h(xmax)])

def danHashtabel(filnavn):
    """
    Returnere en hashtabel ud fra indholdet af en fil.
    @param filnavn en streng med den absolutte sti til en fil med observationer.
    """
    tabel = {}

    # Se om filen eksistere.
    if not(os.path.exists(filnavn)):
        raise ValueError("Filen blev ikke fundet.")

    # Forsøg at læse linjerne i filen, hvis det ikke lykkedes så
    # udskriv passende fejl og returner en tom hashtabel.
    try:
        lines = [line.strip() for line in open(filnavn)]
    except IOError:
        raise IOError("Filen kunne ikke åbnes.")

    # Hvis der ikke var nogen linjer i filen så skriv en passende fejl
    # og returner en tom hashtabel.
    if (len(lines) < 1):
        raise ValueError("Filen var tom.")

    # Parse alle linjerne, eller smid en fejl for ugyldigt syntax.
    for line in lines:
        try:
            x = line.split(',')[0].strip()
            y = line.split(',')[1].strip()
            tabel[x] = y
        except:
            raise Exception(u"Filen har ugyldigt syntax, sørg for formatet 'x.xx , y.yy'")
    # Returner hashtabellen.
    return tabel

def main(args):
    """
    Main function for at tillade brug som modul og som kørtbart script.
    """

    sti = u"flueæg.txt"


    # Kode fra ugesedlen.
    tabel = danHashtabel(sti)
    xs,ys = zip(*tabel.items())
    analyse = linRegrAn(tabel)

    plt.plot(xs,ys,'b^',label=u"Datapunkter fra måling.")
    plt.plot(* analyse, label=u"Linear regressionsanalyse af data.")

    plt.xlabel(u"Luftfugtighed i %")
    plt.ylabel(u"Antal timer for udklækning")
    plt.title(u"Flueægs udklækningstid som en funktion af  luftfugtigheden")
    plt.legend(loc=1, borderaxespad=0.)

    plt.show()
    return 0
if __name__ == '__main__':
    main(sys.argv)
