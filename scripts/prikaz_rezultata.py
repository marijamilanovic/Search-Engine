def unos_broja_stranica_za_prikaz():
    while True:
        try:
            unos = int(input("Unesite broj HTML linkova koji zelite da prikazete po stranici prikaza: "))
        except ValueError:
            print("Pogresan unos!")
            continue
        except KeyboardInterrupt:
            return 1

        if unos > 0:
            return unos
        else:
            print("Uneti broj je manji od 0!")


def prikazi_rezultate(lista_rangiranih, broj_po_str):
    linkovi_po_stranici = broj_po_str
    broj_stranice = (len(lista_rangiranih) // linkovi_po_stranici) - 1

    trenutni = 0
    while True:
        print("--" * 70)
        print("{:130}      {:4}".format("HTML page", "RANG"))

        for i in range(trenutni * linkovi_po_stranici, trenutni * linkovi_po_stranici + linkovi_po_stranici):
            if i < len(lista_rangiranih):
                l = lista_rangiranih[i]
                print("{:130}      {:4}".format(str(l[0]), str(l[1])))

        print("--" * 70)
        print("\nOpcije:\n(+) prikaz sledecih N stranica\n(-) prikaz prethonih N stranica")
        print("(n) promena broja stranica koje se prikazuju\n(e) izlaz")

        while True:
            try:
                unos = str(input(">> "))
            except KeyboardInterrupt:
                print("Pogresan unos!")

            if unos == "e":
                return
            elif unos == "+":
                if trenutni + 1 > broj_stranice:
                    print("Na poslednjoj ste stranici!")
                else:
                    trenutni += 1
                    break
            elif unos == "-":
                if trenutni - 1 < 0:
                    print("Na prvoj ste stranici!")
                else:
                    trenutni -= 1
                    break
            elif unos == "n":
                linkovi_po_stranici = unos_broja_stranica_za_prikaz()
                num_page = (len(lista_rangiranih) // linkovi_po_stranici) - 1
                current_i = 0
                break
            else:
                print("Pogresan unos!")


def prikazi(lista_rangiranih_rez):
    while True:
        try:
            unos = input("Da li zelite da prikazete rezultate? [Yes/No]: ")
        except KeyboardInterrupt:
            return 0

        if unos == "Yes" or unos == "yes" or unos == "Y" or unos == "y":
            print("Ukupan broj stranica iz pretrage [{}]".format(len(lista_rangiranih_rez)))
            br_stranica = unos_broja_stranica_za_prikaz()
            prikazi_rezultate(lista_rangiranih_rez, br_stranica)
            break
        elif unos == "No" or unos == "no" or unos == "n" or unos == "N":
            break
        else:
            print("Pogresan unos!")
