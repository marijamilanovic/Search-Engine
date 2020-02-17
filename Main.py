
if __name__ == "__main__":
    running = True
    userInput = None

    while running:
        print("")
        print("-----------------------")
        print("MENU:")
        print("0 - Kraj")
        print("1 - Parsiranje html fajla")
        print("2 - proba")

        userInput = input("Izaberi broj opcije ->   ")

        if userInput == "1":
            print("parse")

        if userInput == "2":
            print("proba")

        if userInput == "0":
                running = False
