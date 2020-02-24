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
    # os.chdir("whatsnew")
    path = os.path.abspath("")
    print("Pocetna putanja je : {}".format(path))
    dictionary, graf = parsiraj_html(path)

    while running:
        print("")
        print("-----------------------")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Promena direktorijuma")
        print("2 - Parsiranje zadatih HTML fajlova")
        print("3 - Unos 1/vise upita")
        print("4 - Unos logickih upita")

        userInput = input("Izaberi broj opcije ->  ")

        if userInput == "1":
            putanja = input("Unesite direktorijum za parsiranje:")
            if os.path.exists(putanja):
                print("Uspesno promenjena putanja!")
                path = putanja
                dictionary, graf = parsiraj_html(path)

                print("Trenutna putanja je : {}".format(path))
            else:
                print("Putanja ne postoji!")
        elif userInput == "2":
            print("pr. C:\\Users\\MASHA\\test\\py-html")
            print("Unesite direktorijum za parsiranje/indeksiranje:")
            putanja = input()
            if(os.path.exists(putanja)):
                pocetak = time.time()
                dictionary, graf = parsiraj_html(putanja)
                ttime = time.time() - pocetak
                print("Vreme parsiranja fajlova: " + str(ttime) + " sekudni.")
            else:
                print("Dati link direktorijuma nije validan...")
            


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
