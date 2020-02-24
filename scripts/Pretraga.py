from scripts.Parsiranje import *
from structs.set import *

logicalOperators = ["and", "or", "not"]

def standardQuery(inDir, inWord):
    if(len(inWord) > 0):
        sub_str = inWord.split(" ")
        if(len(sub_str) > 1 and (sub_str[1].lower() in logicalOperators) and len(sub_str)==3):
            running = True
            print("Uneli ste logicki ali ne brinite, izvrsava i to")
            print("1 - Nastaviti")
            print("0 - Izadji")
            userInput = input("1 ili 0 --->  ")
            if userInput == "1":
                logicalQuery(inDir, inWord)
                return
            if userInput == "0":
                return None
            elif(userInput!="0" and userInput!="1"):
                print("Greska pri unosu...")
                return None
        for i in range(len(sub_str)):                                   # OVO JE OSTAAAAALOO
            print(str(i+1) + ". rec je " + str(sub_str[i]))
            ispars, curr = newDictionary(sub_str[i], inDir)
            if(curr == 0):
                return None
    else:
        print("Niste nista uneli!")
        return None


def logicalQuery(inDir, inWord):
    if (len(inWord) > 0):
        sub_str = inWord.split(" ")
        if(len(sub_str) > 1 and (sub_str[1] in logicalOperators) and len(sub_str)==3):
            print("Postoji logicki operator (" + sub_str[1] +")")
            if(sub_str[1].lower() in logicalOperators[0]):
                ispars1, curr1 = newDictionary(sub_str[0], inDir)
                ispars2, curr2 = newDictionary(sub_str[2], inDir)
                if(curr1 == 0 or curr2 == 0):
                    return None                                                 # da li vratiti None ili vratiti onog koji sadrzi tu rec
                searchAND(ispars1, ispars2)
            elif(sub_str[1].lower() in logicalOperators[1]):
                ispars1, curr1 = newDictionary(sub_str[0], inDir)
                ispars2, curr2 = newDictionary(sub_str[2], inDir)
                if(curr1 == 0 or curr2 == 0):
                    return None
                searchOR(ispars1, ispars2)
            elif(sub_str[1].lower() in logicalOperators[2]):
                ispars1, curr1 = newDictionary(sub_str[0], inDir)
                ispars2, curr2 = newDictionary(sub_str[2], inDir)
                if (curr1 == 0 or curr2 == 0):
                    return None
                searchNOT(ispars1, ispars2)
        elif(len(sub_str) == 1 or len(sub_str)>1):
            print("Nema logickih operatora, pa se gleda kao STANDARDNI UPIT")
            standardQuery(inDir, inWord)
    else:
        print("Niste nista uneli!")
        return None



def searchAND(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    for key1 in dict1.keys():
        set1.add(key1)
    for key2 in dict2.keys():
        set2.add(key2)
    rezz = set1.intersection(set2)
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)


def searchOR(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    for key1 in dict1.keys():
        set1.add(key1)
    for key2 in dict2.keys():
        set2.add(key2)
    rezz = set1.union(set2)
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)


def searchNOT(dict1, dict2):
    set1 = Set()
    set2 = Set()
    rezz = Set()
    for key1 in dict1.keys():
        set1.add(key1)
        #print(key1)
    #print("*********")
    for key2 in dict2.keys():
        set2.add(key2)
        #print(key2)
    #print("*********")
    rezz = set2.difference(set1)        # u zagradi je onaj ciji ce se skup prikazati (bez ovog drugog)
    print("---- REZULTUJUCI SKUP HTML STRANICA ----")
    for kk in rezz.__iter__():
        pri = ispisNazivaFajla(kk)
        print(pri)



    '''
    for i in  range(2, 100, 2):
        if(sub_str[i] in logicalOperators[0]):

            # pretraga za AND
        if(sub_str[i] in logicalOperators[1]):

        if(sub_str[i] in logicalOperators[2]):

        else:
            #pozovi standardnu pretragu
    '''


