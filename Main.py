from time import time
from scripts.Pretraga import *
from scripts.Parsiranje import *
from scripts.prikaz_rezultata import prikazi_rezultate, prikazi
from scripts.rang import rang
from scripts.sort import sort

if __name__ == "__main__":
    running = True
    userInput = None
    dictionary = None
    graf = None

    os.chdir("test-skup")
    os.chdir("python-2.7.7-docs-html\whatsnew")
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
                print("Prvo morate PARSIRATI, pritisnite broj 1 !!!")
            else:
                inSQ = str(input("Unesi rec ->  "))
                standardQuery(dictionary, inSQ)
                print(dictionary)


        elif userInput == "3":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1 !!!")
            else:
                inLQ = str(input("Unesi rec ->  "))
                logicalQuery(dictionary, inLQ)


        elif userInput == "4":
            rec = input("Unesite rec:")
            res = standardQuery(dictionary, rec)

            if len(res) > 0:
                rang_rezultat = rang(graf, res)
                lista_rangiranih_resultata = list(rang_rezultat.items())
                sort(lista_rangiranih_resultata, 0, len(lista_rangiranih_resultata) - 1)
                prikazi(lista_rangiranih_resultata)
            else:
                print("--" * 50)
                print("Pretraga je neuspesna!")
                print("--" * 50)

        elif userInput == "0":
                running = False


        elif(userInput!="0" and userInput!="1" and userInput!="2" and userInput!="3" and userInput!="4"):
            print("GRESKA PRI UNOSU !")
