from Trie import *
from Parsiranje import *

logicalOperators = ["AND", "OR", "NOT"]                         # da li logicki operatori mogu biti i malim i velikim slovima napisani ?

def standardQuery(inDir, inWord):
    sub_str = inWord.split(" ")
    for i in range(len(sub_str)):
        print(str(i+1) + ". rec je " + str(sub_str[i]))
        parsirajQ(inDir, inWord)


def logicalQuery(userInput):                                    # SKICA
    sub_str = userInput.split(" ")
    firstWord = sub_str[0]
    secondWord = sub_str[1]
    thirdWord = sub_str[2]

    if(secondWord in logicalOperators):
        print("Postoji logicki operator (" + secondWord +")")

        if(secondWord == logicalOperators[0]):
            print("Kod za AND")
        if(secondWord == logicalOperators[1]):
            print("Kod za OR")
        else:
            print("Onda je NOT")

    else:
        print("Greska")                                                     # ili normalna rec



    '''
    for i in  range(2, 100, 2):
        if(sub_str[i] in logicalOperators[0]):

            # pretraga za AND
        if(sub_str[i] in logicalOperators[1]):

        if(sub_str[i] in logicalOperators[2]):

        else:
            #pozovi standardnu pretragu
    '''


