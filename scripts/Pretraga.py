from scripts.Parsiranje import *
from structs.set import *

logicalOperators = ["and", "or", "not"]


def standardQuery(inDir, inWord):
    if (len(inWord) > 0):
        sub_str = inWord.split()                                            # nebitno koliko razmaka korisnik unese
        if (len(sub_str) > 1 and (sub_str[1].lower() in logicalOperators) and len(sub_str) == 3):
            print("Uneli ste logicki ali ne brinite, izvrsava i to")
            print("1 - Nastaviti")
            print("0 - Izadji")
            userInput = input("1 ili 0 --->  ")
            if userInput == "1":
                logicalQuery(inDir, inWord)
                return
            if userInput == "0":
                return None
            elif (userInput != "0" and userInput != "1"):
                print("Greska pri unosu...")
                return None
        if (len(sub_str) == 1):                                             # 1 rec
            print("Rec je " + str(sub_str[0]))
            ispars, curr = newDictionary(sub_str[0].lower(), inDir)
            if (curr == 0):
                return None
            return ispars
        if (len(sub_str) == 2 and (sub_str[0] != sub_str[1])):              # 2 reci
            ispars1, curr1 = newDictionary(sub_str[0].lower(), inDir)
            ispars2, curr2 = newDictionary(sub_str[1].lower(), inDir)
            if (curr1 == 0 or curr2 == 0):
                return None
            finito = searchOR(ispars1, ispars2)
            return finito
        if (len(sub_str) == 3 and (sub_str[0] != sub_str[1] and sub_str[1] != sub_str[2] and sub_str[0] != sub_str[2])):
            ispars1, curr1 = newDictionary(sub_str[0].lower(), inDir)       # 3 reci
            ispars2, curr2 = newDictionary(sub_str[1].lower(), inDir)
            ispars3, curr3 = newDictionary(sub_str[2].lower(), inDir)
            if (curr1 == 0 or curr2 == 0 or curr3 == 0):
                return None
            finito = searchStandardOR(ispars1, ispars2, ispars3)
            return finito
        else:
            print("Greska prilikom unosa...")
    else:
        print("Niste nista uneli!")
        return None


def logicalQuery(inDir, inWord):
    if (len(inWord) > 0):
        sub_str = inWord.split()
        if (len(sub_str) > 1 and (sub_str[1].lower() in logicalOperators) and len(sub_str) == 3):
            print("Postoji logicki operator (" + sub_str[1] + ")")
            if (sub_str[1].lower() in logicalOperators[0]):         # AND
                ispars1, curr1 = newDictionary(sub_str[0].lower(), inDir)
                ispars2, curr2 = newDictionary(sub_str[2].lower(), inDir)
                if (curr1 == 0 or curr2 == 0):
                    return None
                finito = searchAND(ispars1, ispars2)
                return finito
            elif (sub_str[1].lower() in logicalOperators[1]):       # OR
                ispars1, curr1 = newDictionary(sub_str[0].lower(), inDir)
                ispars2, curr2 = newDictionary(sub_str[2].lower(), inDir)
                if (curr1 == 0 or curr2 == 0):
                    return None
                finito = searchOR(ispars1, ispars2)
                return finito
            elif (sub_str[1].lower() in logicalOperators[2]):       # NOT
                ispars1, curr1 = newDictionary(sub_str[0].lower(), inDir)
                ispars2, curr2 = newDictionary(sub_str[2].lower(), inDir)
                if (curr1 == 0 or curr2 == 0):
                    return None
                finito = searchNOT(ispars1, ispars2)
                return finito
        elif (len(sub_str) == 1 or len(sub_str) > 1):                           # omoguceno prebacivanje na standardni upit
            print("Nema logickih operatora, pa se gleda kao STANDARDNI UPIT")   # korisnik bira
            print("Da li zelite da se izvrsi kao obican upit?")
            print("1 - Nastaviti")
            print("0 - Izadji")
            userInput = input("1 ili 0 --->  ")
            if userInput == "1":
                standardQuery(inDir, inWord)
                return
            if userInput == "0":
                return None
            elif (userInput != "0" and userInput != "1"):
                print("Greska pri unosu...")
                return None
    else:
        print("Niste nista uneli!")
        return None


def searchAND(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    finito = {}
    for key1 in dict1.keys():
        set1.add(key1)
        dict1[key1] = dict1[key1]
    for key2 in dict2.keys():
        set2.add(key2)
        dict2[key2] = dict2[key2]
    rezz = set1.intersection(set2)
    for i in dict1.keys():                              # presek prvog i drugog
        if i in dict2.keys():
            finito[i] = dict1[i] + dict2[i]             # sabiranje njihovih vrednosti
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)
    return finito




def searchOR(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    finito = {}
    for key1 in dict1.keys():
        set1.add(key1)
    for key2 in dict2.keys():
        set2.add(key2)
    rezz = set1.union(set2)
    for i in dict1.keys():                      # prvo uradimo uniju
        if i in dict2.keys():
            finito[i] = dict1[i] + dict2[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict1.keys():                       # ako su samo u prvom
        if i not in dict2.keys():
            finito[i] = dict1[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict2.keys():                      # ako su samo u drugom
        if i not in dict1.keys():
            finito[i] = dict2[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)
    return finito


def searchStandardOR(dict1, dict2, dict3):
    set1 = Set()
    set2 = Set()
    set3 = Set()
    rezz = Set()
    finito = {}
    for key1 in dict1.keys():
        set1.add(key1)
    for key2 in dict2.keys():
        set2.add(key2)
    for key3 in dict3.keys():
        set3.add(key3)
    rezz = set1.union(set2.union(set3))                                         # presek sva tri
    for i in dict1.keys():
        if i in dict2.keys():
            if i in dict3.keys():
                finito[i] = dict1[i] + dict2[i] + dict3[i]
                #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict1.keys():                                                      # samo u prvom
        if((i not in dict2.keys()) and (i not in dict3.keys())):
                finito[i] = dict1[i]
                #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict2.keys():
        if((i not in dict1.keys()) and (i not in dict3.keys())):                # samo u drugom
                finito[i] = dict2[i]
                #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict3.keys():                                                      # samo u trecem
        if((i not in dict1.keys()) and (i not in dict2.keys())):
                finito[i] = dict3[i]
                #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict1.keys():                                                      # presek 1. i 2.
        if((i in dict2.keys()) and (i not in dict3.keys())):
            finito[i] = dict1[i] + dict2[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict1.keys():                                                      # presek 1. i 3.
        if((i in dict3.keys()) and (i not in dict2.keys())):
            finito[i] = dict1[i] + dict3[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    for i in dict2.keys():                                                      # presek 2. i 3.
        if((i in dict3.keys()) and (i not in dict1.keys())):
            finito[i] = dict2[i] + dict3[i]
            #print("kljuc: " + str(i) + " ------ " + str(finito[i]))
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)
    return finito


def searchNOT(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    finito = {}
    for key1 in dict1.keys():
        set1.add(key1)
    for key2 in dict2.keys():
        set2.add(key2)
    rezz = set2.difference(set1)                # u zagradi je onaj ciji ce se skup prikazati (bez ovog drugog)
    for key, value in dict1.items():            # ako je kljuc u prvom a nije u drugom skupu (odnosno recniku)
        if key not in dict2.keys():
            finito[key] = value
            #print("kljuc: " + str(key) + " ------ " + str(value))
    #print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)
    return finito

    '''
    for i in  range(2, 100, 2):
        if(sub_str[i] in logicalOperators[0]):

            # pretraga za AND
        if(sub_str[i] in logicalOperators[1]):

        if(sub_str[i] in logicalOperators[2]):

        else:
            #pozovi standardnu pretragu

    if(len(sub_str) > 2):
            print("1. rec je " + str(sub_str[0]))
            ispars1, curr1 = newDictionary(sub_str[0], inDir)
            print(ispars1)
            print("2. rec je " + str(sub_str[1]))
            ispars2, curr2 = newDictionary(sub_str[1], inDir)
            print(ispars2)
            if (curr1 == 0 && curr2 == 0):
                return None
            for i in range(2, len(sub_str)):
                print(str(i+2) + ". rec je " + str(sub_str[i]))
                ispars3, curr1 = newDictionary(sub_str[i], inDir)
                if(curr3 == 0):
                    return None
                print(ispars3)
                ispars2.update(ispars2)
            print("*************")
            print("ovo je bitno " + str(ispars2))

    #for i in range(len(sub_str)):                                   # OVO JE OSTAAAAALOO
                #print(str(i+1) + ". rec je " + str(sub_str[i]))
                #ispars, curr = newDictionary(sub_str[i], inDir)
                #if(curr == 0):
                    #return None
            #print()

    '''


