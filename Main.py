from time import time
from scripts.Pretraga import *
from scripts.Parsiranje import *


if __name__ == "__main__":
    running = True
    userInput = None
    dictionary = None
    graf = None

    os.chdir("test-skup")
    os.chdir("python-2.7.7-docs-html")
    #os.chdir("whatsnew")
    path = os.path.abspath("")
    print("Pocetna putanja je : {}".format(path))
    dictionary, graf = parsiraj_html(path)

    while running:
        print("")
        print("-----------------------")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Promena direktorijuma")
        print("2 - Unos 1/vise upita")
        print("3 - Unos logickih upita")
        print("4 - Rangirana pretraga")

        userInput = input("Izaberi broj opcije ->  ")

        if userInput == "1":
            putanja = input("Unesite direktorijum za parsiranje:  ")
            if os.path.exists(putanja):
                path = putanja
                dictionary, graf = parsiraj_html(path)
                print("Uspesno promenjena putanja!")
                print("Trenutna putanja je : {}".format(path))
            else:
                print("Putanja ne postoji!")


        elif userInput == "2":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inSQ = str(input("Unesi rec ->  "))
                standardQuery(dictionary, inSQ)


        elif userInput == "3":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inLQ = str(input("Unesi rec ->  "))
                logicalQuery(dictionary, inLQ)



        elif userInput == "0":
                running = False


        elif(userInput!="0" and userInput!="1" and userInput!="2" and userInput!="3" and userInput!="4"):
            print("GRESKA PRI UNOSU !")
