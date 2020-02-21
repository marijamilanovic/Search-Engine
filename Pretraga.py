from Trie import *
from Parsiranje import *


logicalOperators = ["AND", "OR", "NOT", "and", "or", "not"]

def standardQuery(inDir, inWord):
    if(len(inWord) > 0):
        sub_str = inWord.split(" ")
        if(len(sub_str) > 1):
            if((sub_str[1] in logicalOperators) and len(sub_str)==3):
                running = True
                print("Uneli ste logicki ali ne brinite, izvrsava i to")
                print("1 - Nastaviti")
                print("0 - Izadji")
                userInput = input("1 ili 0 --->  ")
                while running:
                    if userInput == "1":
                        logicalQuery(inDir, inWord)
                    if userInput == "0":
                        running == False
        for i in range(len(sub_str)):
            print(str(i+1) + ". rec je " + str(sub_str[i]))
            ispars = parsirajQ(inDir, sub_str[i])
            #print(ispars)
    else:
        print("Niste nista uneli!")
        return None #
                                                                                # kada Milica odradi RANGIRANJE treba ispisati pretragu OR

def logicalQuery(inDir, inWord):                                    # SKICA
    sub_str = inWord.split(" ")
    if((sub_str[1] in logicalOperators) and len(sub_str)==3):
        print("Postoji logicki operator (" + sub_str[1] +")")
        if(sub_str[1] == logicalOperators[0]):                              # AND
            ispars1 = parsirajQ(inDir, sub_str[0])
            ispars1 = set()
            ispars2 = parsirajQ(inDir, sub_str[2])
            #recnik = ispars1.union(ispars2)

        elif(sub_str[1] == logicalOperators[1]):
            print("Kod za OR")
        else:
            print("Onda je NOT")
    else:
        print("Nemate logickih operatore. Gleda se kao standardni upit...")
        standardQuery(inDir, inWord)                                          # ili normalna rec



    '''
    for i in  range(2, 100, 2):
        if(sub_str[i] in logicalOperators[0]):

            # pretraga za AND
        if(sub_str[i] in logicalOperators[1]):

        if(sub_str[i] in logicalOperators[2]):

        else:
            #pozovi standardnu pretragu
    '''


