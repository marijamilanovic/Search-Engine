from time import time
from scripts.Pretraga import *



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
        print("3 - Unos 1/vise upita")                                      # nije gotovo
        print("4 - Unos logickih upita")                                    # nije gotovo

        userInput = input("Izaberi broj opcije ->   ")

        if userInput == "1":
            start_time = time()
            dictionary = parsiraj()
            end_time = time()
            ttime = end_time - start_time
            print("Vreme parsiranja fajlova: " + str(ttime) + " sekudni.")


        if userInput == "2":
            print("pr. C:\\Users\\MASHA\\test\\py-html")
            myInput = str(input("Puna lokacija foldera ->  "))
            if(os.path.exists(myInput)):
                startTime = time()
                dictionary = parsirajZadato(myInput)
                endTime = time()
                timee = endTime - startTime
                print("Vreme parsiranja fajlova: " + str(timee) + " sekudni.")
            else:
                print("Dati link ka folderu nije validan...")


        if userInput == "3":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inSQ = str(input("Unesi rec ->  "))
                standardQuery(dictionary, inSQ)


        if userInput == "4":
            if (dictionary == None):
                print("Prvo morate PARSIRATI, pritisnite broj 1  ili 2 !!!")
            else:
                inLQ = str(input("Unesi rec ->  "))
                logicalQuery(dictionary, inLQ)


        if userInput == "0":
                running = False


        elif(userInput!="0" and userInput!="1" and userInput!="2" and userInput!="3" and userInput!="4"):
            print("GRESKA PRI UNOSU !")
