
from Parsiranje import *
from time import time



if __name__ == "__main__":
    running = True
    userInput = None

    while running:
        print("")
        print("-----------------------")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiranje HTML fajlova iz test skupa")
        print("2 - Parsiranje zadatih HTML fajlova")
        print("3 - ")

        userInput = input("Izaberi broj opcije ->   ")

        if userInput == "1":
            start_time = time()
            parsiraj()
            end_time = time()
            ttime = end_time - start_time
            print("Vreme parsiranja fajlova: " + str(ttime) + " sekudni.")


        if userInput == "2":
            print("pr. C:\\Users\\MASHA\\test\\py-html")
            myInput = str(input("Puna lokacija foldera ->  "))
            startTime = time()
            parsirajZadato(myInput)
            endTime = time()
            timee = endTime - startTime
            print("Vreme parsiranja fajlova: " + str(timee) + " sekudni.")

        if userInput == "0":
                running = False
