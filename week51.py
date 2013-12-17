#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ugeopgave for uge 51 af Martin Jørgensen and Sarah Vang Nøhr.

# Vi har valgt at bruge en liste af lister af bools til at repræsentere verden,
# fordi det var den mest naturlige løsning da man så kan indeksere ind i
# verden som om det var en matrice, f.eks. verden[m][n].
# Vi har valgt at lave en konstant størrelse på verden. Da man alligevel ville
# være nødt til at lave en øvre grænse for simulationen, virkede det logisk  at
# at lave en fast størrelse fra starten, så man lettere kunne udregne de
# forventede resultater af simulationen.
# Vi har valgt at lave en flad verden. Det giver en mere overskuelig kode, og
# sætter mere fokus på selve "spillet" og hvordan reglerne fungerer, da der ikke
# pludseligt opstår nye levende celler ude ved kanterne. Derudover giver en rund
# verden giver ikke noget ekstra til simulationen, det gør den blot anderledes.

import sys
from copy import deepcopy
from kursusuge5modul import *

verden = []

def antalNaboer(i,j):
    """
    Returnerer antallet af levende naboer cellen (i,j) har.
    Returnerer 0 hvis (i,j) er uden for verdenen.
    """
    global verden
    naboer = 0
    if levende(i-1, j+1):
        naboer += 1
    if levende(i  , j+1):
        naboer += 1
    if levende(i+1, j+1):
        naboer += 1
    if levende(i-1, j):
        naboer += 1
    if levende(i+1, j):
        naboer += 1
    if levende(i-1, j-1):
        naboer += 1
    if levende(i  , j-1):
        naboer += 1
    if levende(i+1, j-1):
        naboer += 1
    return naboer

def foerste():
    """
    Befolker verdenen med den første generation.
    Returnere en kvadruble:
    (i_min, i_max, j_min, j_max)
    som er størrelsen på verdenen.
    """
    global verden
    verden = []
    imin = 0
    imax = 10
    jmin = 0
    jmax = 10
    for i in range(imax):
        midl = []
        for j in range(jmax):
            midl.append(False)
        verden.append(midl)
    return (imin, imax-1, jmin, jmax-1)

def naeste():
    """
    Beregner næste generation i spillet og opdatere verdenen.
    Returnere en kvadruble:
    (i_min, i_max, j_min, j_max)
    som er størrelsen på verdenen.
    """
    global verden
    midlVerden = deepcopy(verden)
    for i in range(len(verden)):
        for j in range(len(verden[i])):
            naboer = antalNaboer(i,j)
            if not(levende(i,j)) and naboer == 3:
                midlVerden[i][j] = True
            if levende(i,j) and naboer < 2 or naboer > 3:
                midlVerden[i][j] = False
    verden = midlVerden

    imin = 0
    if len(verden) == 0:
        imin = -1
    imax = len(verden)-1
    if imax >= 0:
        jmax = len(verden[0])-1
        if jmax >= 0:
            jmin = 0
    else:
        jmin = -1
        jmax = -1
    return (imin, imax, jmin, jmax)

def levende(i,j):
    """
    Kontrollerer om cellen (i,j) er levende.
    Returnerer True hvis den er, False ellers.
    Hvis i eller j er ude for verdenen vil den returnere False.
    """
    global verden
    if (i >= len(verden)) or (i < 0):
        return False
    if (j >= len(verden[i])) or (j < 0):
        return False
    return verden[i][j]

def klik(i,j):
    """
    "omvender" et felt, dvs fra død til levende og omvendt.
    Gør intet hvis (i,j) er udenfor den begrænsede verden.
    """
    global verden
    if (i >= len(verden)) or (i < 0):
        return
    if (j >= len(verden[i])) or (j < 0):
        return
    verden[i][j] = not(verden[i][j])
    return

def main(args):
    """
    Main function for at tillade brug som modul og som kørtbart script.
    """
    # Test for foerste
    imin,imax,jmin,jmax = foerste()
    res = True
    res = res and (len(verden) == 10)
    res = res and (len(verden[0]) == 10)
    if res:
        print "(V) Verden har korrekte dimensioner."
    else:
        print "(F) Verden har forkerte dimensioner, foerste() er i stykker."

    res = True
    res = res and imin == 0
    res = res and imax == 9
    res = res and jmin == 0
    res = res and jmax == 9
    if res:
        print "(V) foerste() returnerer korrekte dimensioner."
    else:
        print "(F) foerste() returnerer forkerte dimensioner."

    res = False
    for i in range(len(verden)):
        for j in range(len(verden[i])):
            res = res or verden[i][j]
    if not(res):
        print "(V) Verden er korrekt initialiseret, alt er dødt."
    else:
        print "(F) Verden er ikke korrekt initialiseret, noget lever, foerste() er i stykker."


    # Tests for naeste
    verden[0][0] = True
    imin,imax,jmin,jmax = naeste()
    res = True
    res = res and (len(verden) == 10)
    res = res and (len(verden[0]) == 10)
    if res:
        print "(V) Verden har korrekte dimensioner."
    else:
        print "(F) Verden har forkerte dimensioner, naeste() er i stykker."

    res = True
    res = res and imin == 0
    res = res and imax == 9
    res = res and jmin == 0
    res = res and jmax == 9
    if res:
        print "(V) naeste() returnerer korrekte dimensioner."
    else:
        print "(F) naeste() returnerer forkerte dimensioner."

    res = False
    for i in range(len(verden)):
        for j in range(len(verden[i])):
            res = res or verden[i][j]
    if not(res):
        print "(V) Alt er dødt naeste() virker."
    else:
        print "(F) Noget lever, naeste() er i stykker."

    verden[0][0] = True
    verden[0][2] = True
    verden[2][1] = True
    naeste()
    res = True
    res = res and (verden[0][0] == False)
    res = res and (verden[0][2] == False)
    res = res and (verden[2][1] == False)
    res = res and verden[1][1]
    if res:
        print "(V) naeste() bruger reglerne korrekt."
    else:
        print "(F) naeste() bruger reglerne forkert."

    # Tests for levende
    if levende(1,1):
        print "(V) levende() virker."
    else:
        print "(F) levende() virker ikke."

    # Tests for klik
    klik(1,1)
    if not(levende(1,1)):
        print "(V) klik() virker."
    else:
        print "(F) klik() virker ikke."

    # LET THE GAMES BEGIN!!!
    visLife(foerste,naeste,levende,klik)
    return 0

if __name__ == '__main__':
    main(sys.argv)
