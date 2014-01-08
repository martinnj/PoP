#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Ugeopgave for uge 1 af Martin Jørgensen og Sarah Vang Nøhr.

import sys

class simplematrix:
    """
    Simpel matrice klasee som indeholder grunlæggende lineær algebra
    funktioner.
    """
    vaerdier = []
    m = 0
    n = 0
    def __init__(self, m  = 0, n = 0, vaerdier = []):
        """
Der er 3 brugstilfælde af denne konstruktør:
0 simplematrix()
(PreCondition)
Intet, bare kald den du.
(PostCondition)
Uddata: en 0x0 matrice uden værdier (sjovt nok).

1 simplematrix(m, n):
(PreCondition)
Inddata: m antal rækker matricen skal have, hvor m > 0.
Inddata: n antal kolonner matricen skal have, hvor n > 0.
(PostCondition)
Uddata: en mxn matrice hvor alle værdier er 0.

2 simplematrix(m, n, vaerdier)
(PreCondition)
Inddata: m antal rækker matricen skal have, hvor m > 0.
Inddata: n antal kolonner matricen skal have, hvor n > 0.
Inddata: vaerdier En integer liste med værdier  der tildeles cellerne i matricen. Listen skal være m*n lang.
(PostCondition)
Uddata: en mxn matrice hvor alle værdier er draget i rækkefølge fra listen.
        """
        self.m = m
        self.n = n
        self.vaerdier = []
        k = 0
        harVaerdier = False
        antalVaerdier = len(vaerdier)
        if (antalVaerdier > 0):
            if (antalVaerdier != m*n):
                raise ValueError("Antallet af værdier er ikke det samme som antallet af celler i den ønskede matrice.")
            harVaerdier = True
        for i in range(m):
            tmp = []
            for j in range(n):
                if (harVaerdier):
                    tmp.append(vaerdier[k])
                    k = k + 1
                else:
                    tmp.append(0)
            self.vaerdier.append(tmp)

    def __str__(self):
        """
Returnere matricen i letlæselig strengform.
(PostCondition)
Uddata: en string med værdierne i matricen i tabelformat.
        """
        res = ""
        for i in range(self.m):
            for j in range(self.n):
                res = res + str(self.vaerdier[i][j])
                if (j < self.n - 1):
                    res = res + ","
            if (i < self.m - 1):
                res = res + "\n"
        return res

    def read(self, sti):
        """
Læser en matrice fra en fil.
(PreCondition)
Inddata: sti En streng med en gyldig sti til en fil af formatet :
1,2,3,4
5,6,7,8
9,10,11,12
Dvs. en mxn matrice bygget af linjer som rækker, med kommaseparerede tal som søjler,
eller en tom fil.
(PostCondition)
Matricen er opdateret med værdierne og størrelsen fra filen.
Hvis der fremkommer en exception når filen tilgås vil funktionen returnere
og matricen vil være uændret.
        """
        self.vaerdier = []
        try:
            f = open(sti,'r')
        except:
            raise IOError("Filen: \"" + sti + "\" kunne ikke læses. Matricens indhold er urørt.")

        for line in f:
            tmp = line.strip().split(',')
            if (len(tmp) >0) and (tmp[0] <> ''):
                tmp = map(int,tmp)
            self.vaerdier.append(tmp)
        self.m = len(self.vaerdier)
        self.n = len(self.vaerdier[0])
        try:
            f.close()
        except IOError as ex:
            raise IOError("Kunne ikke lukke filen: \"" + sti + "\" : " + ex.message)

    def write(self, sti):
        """
Skriver en matrice til en fil.
(PreCondition)
Inddata: sti En streng med en gyldig sti til, hvor matricen skal gemmes.
(PostCondition)
Matricen er skrevet til den angivne fil.
Hvis filen der forsøges at skrive til en ugyldig sti vil en IOError blive kastet.
Hvis der opstår en fejl under skrivning eller lukning af filen vil en IOError blive kastet.
        """
        try:
            f = open(sti,'wb')
        except IOError as ex:
            raise IOError("\"" + sti + "\" Kunne ikke åbnes: " + ex.message)
        try:
            f.write(self.__str__())
            f.write("\n")
        except IOError as ex:
            raise IOError("Der skete en fejl under skrivning til \"" +sti + "\" : " + ex.message)

        try:
            f.close()
        except IOError as ex:
            raise IOError("Kunne ikke lukke filen: \"" + sti + "\" : " + ex.message)


    def __add__(A, B):
        """
Adderer to  matricer.
(PreCondition)
Inddata: A En matrice af størrelsen mxn.
Inddata: B En matrice af størrelsen mxn (dvs. samme størrelse som A).
(PostCondition)
Uddata: En matrice af størrelsen mxn indeholdende de adderede værdier fra A og B.
Hvis matricerne ikke har samme størrelse vil der kastes en ValueError.
        """
        if (A.m != B.m) or (A.n != B.n):
            raise ValueError("Matricerne A og B har forskellige størrelser.")
        tmp = []
        for i in range(A.m):
            for j in range(A.n):
                tmp.append(A.vaerdier[i][j] + B.vaerdier[i][j])
        return simplematrix(A.m, A.n, tmp)

    def __mul__(A, B):
        """
Multiplicerer to matricer.
(PreCondition)
Inddata: A En matrice af størrelsen mxn.
Inddata: B En matrice af størrelsen nxo.
(PostCondition)
Uddata: En matrice af størrelsen mxo indeholdende prikproduktet af A og B.
        """
        C = simplematrix(A.m, B.n)
        for i in range(C.m):
            for j in range(C.n):
                for k in range(A.n):
                    C.vaerdier[i][j] = C.vaerdier[i][j] + A.vaerdier[i][k] * B.vaerdier[k][j]
        return C

#     def __cmp__(A, B):
#         """
# Tjekker, om to matricer er ens.
# (PreCondition)
# Inddata: A En matrice.
# Inddata: B En matrice.
# (PostCondition)
# Uddata: Returnerer True, hvis A og B er ens, ellers returneres False.
#         """
#         return __eq__(A, B)

    def __eq__(A, B):
        """
Tjekker, om to matricer er ens.
(PreCondition)
Inddata: A En matrice.
Inddata: B En matrice.
(PostCondition)
Uddata: Returnerer True, hvis A og B er ens, ellers returneres False.
        """
        if A.m <> B.m:
            return False
        if A.n <> B.n:
            return False
        for i in range(A.m):
            for j in range(A.n):
                if A.vaerdier[i][j] <> B.vaerdier[i][j]:
                    return False
        return True

def main(args):
    """
    Main function for at tillade brug som modul og som kørtbart script.
    """
    print "Nu afprøves den tomme konstruktør."
    A = simplematrix()
    print (A.m == 0) and (A.n == 0) and (A.vaerdier == [])

    print "Nu afprøves den anden konstruktør."
    A = simplematrix(1,1)
    print (A.m == 1) and (A.n == 1) and (A.vaerdier == [[0]])
    print "Nu afprøves den anden konstruktør igen."
    A = simplematrix(2,2)
    print (A.m == 2) and (A.n == 2) and (A.vaerdier == [[0,0],[0,0]])

    print "Nu afprøves den sidste konstruktør."
    A = simplematrix(2 ,2, [1,2,3,4])
    print (A.m == 2) and (A.n == 2) and (A.vaerdier == [[1,2],[3,4]])

    print "Nu afprøves __str__ toString SKRIV MIG funktionen.....Something."
    streng = str(A)
    print streng == "1,2\n3,4"
    print str(simplematrix()) == ""

    print "Nu afprøves lighedsoperatoren."
    B = A
    print A == B
    C = simplematrix()
    print not(A == C)
    C = simplematrix(2, 2, [1,2,100,100])
    print not(A == C)

    print "Nu afprøves matrixaddition af 2 lige store matricer."
    B = simplematrix(2, 2, [5,6,7,8])
    C = simplematrix(2, 2, [6,8,10,12])
    print C == A + B

    print "Nu afprøves matrixmultiplikation af 1x2 og 2x1 matricer."
    A = simplematrix(1, 2, [1,1])
    B = simplematrix(2, 1, [1,1])
    C = simplematrix(1, 1, [2])
    print C == A * B
    print "Nu afprøves matrixmultiplikation af 2x2 og 2x2 matricer."
    A = simplematrix(2, 2, [1,2,3,4])
    B = simplematrix(2, 2, [1,2,5,6])
    C = simplematrix(2, 2, [11,14,23,30])
    print C == A * B

    print "Nu afprøves matrix fil I/O funktionerne."
    A.write("testme.matrix")
    B.read("testme.matrix")
    print A == B

    A = simplematrix(2,3)
    A.write("testme.matrix")
    B = simplematrix()
    B.read("testme.matrix")
    print A == B
    return 0

if __name__ == '__main__':
    main(sys.argv)
