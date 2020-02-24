from time import time
from scripts.Pretraga import *
from scripts.Parsiranje import *


if __name__ == "__main__":
    running = True
    userInput = None
    dictionary = None

    while running:
        print("")
        print("-----------------------")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiranje HTML fajlova iz test skupa")
        print("2 - Parsiranje zadatih HTML fajlova")
        print("3 - Unos 1/vise upita")
        print("4 - Unos logickih upita")

        userInput = input("Izaberi broj opcije ->   ")

        if userInput == "1":
            pocetak = time.time()
            print("Unesite direktorijum za parsiranje/indeksiranje:")
            putanja = input()
            parsiraj_html(putanja)
            ttime = time.time()-pocetak
            print("Vreme: " + str(ttime) + " sekundi.")

        elif userInput == "2":
            print("pr. C:\\Users\\MASHA\\test\\py-html")
            myInput = str(input("Puna lokacija foldera ->  "))
            if(os.path.exists(myInput)):
                startTime = time()
                #dictionary = parsirajZadato(myInput)
                endTime = time()
                timee = endTime - startTime
                print("Vreme parsiranja fajlova: " + str(timee) + " sekudni.")
            else:
                print("Dati link ka folderu nije validan...")


        elif userInput == "3":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inSQ = str(input("Unesi rec ->  "))
                standardQuery(dictionary, inSQ)


        elif userInput == "4":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inLQ = str(input("Unesi rec ->  "))
                logicalQuery(dictionary, inLQ)

        elif userInput == "5":
            pass


        elif userInput == "0":
                running = False


        elif(userInput!="0" and userInput!="1" and userInput!="2" and userInput!="3" and userInput!="4"):
            print("GRESKA PRI UNOSU !")
