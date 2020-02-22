from scripts.Parsiranje import *

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
            if userInput == "0":
                return None
            elif(userInput!="0" and userInput!="1"):
                print("Greska pri unosu...")
                return None
        for i in range(len(sub_str)):
            print(str(i+1) + ". rec je " + str(sub_str[i]))
            #ispars = parsirajQ(inDir, sub_str[i])
            ispars, curr = newDictionary(sub_str[i], inDir)                   # kada Milica odradi RANGIRANJE i SET treba ispisati PRETRAGU ZA OR
            if(curr == 0):
                return None
    else:
        print("Niste nista uneli!")
        return None


def logicalQuery(inDir, inWord):                                    # SKICA
    if (len(inWord) > 0):
        sub_str = inWord.split(" ")
        if(len(sub_str) > 1 and (sub_str[1] in logicalOperators) and len(sub_str)==3):
            print("Postoji logicki operator (" + sub_str[1] +")")
            if(sub_str[1].lower() in logicalOperators[0]):                              # AND
                ispars1, curr1 = newDictionary(sub_str[0], inDir)
                ispars2, curr2 = newDictionary(sub_str[2], inDir)
                if(curr1==0 or curr2==0):
                    return None                                                         # da li vratiti None ili vratiti onog koji sadrzi tu rec
            elif(sub_str[1].lower() in logicalOperators[1]):
                print("Kod za OR")
            elif(sub_str[1].lower() in logicalOperators[2]):
                print("Onda je NOT")
        elif(len(sub_str) == 1 or len(sub_str)>1):
            print("Nema logickih operatora, pa se gleda kao STANDARDNI UPIT")
            standardQuery(inDir, inWord)
    else:
        print("Niste nista uneli!")
        return None



    '''
    for i in  range(2, 100, 2):
        if(sub_str[i] in logicalOperators[0]):

            # pretraga za AND
        if(sub_str[i] in logicalOperators[1]):

        if(sub_str[i] in logicalOperators[2]):

        else:
            #pozovi standardnu pretragu
    '''


