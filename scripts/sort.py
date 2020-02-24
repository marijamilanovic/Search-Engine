def podela(rezultat, najmanji, najveci):
    i = najmanji - 1
    pivot = rezultat[najveci]

    for j in range(najmanji, najveci):
        element = rezultat[j]
        if element[1] > pivot[1]:
            i = i + 1
            rezultat[i], rezultat[j] = rezultat[j], rezultat[i]
    rezultat[i+1], rezultat[najveci] = rezultat[najveci], rezultat[i+1]

    return i+1


def sort(rezultat, najmanji, najveci):
    if najmanji < najveci:
        p = podela(rezultat, najmanji, najveci)

        sort(rezultat, najmanji, p - 1)
        sort(rezultat, p + 1, najveci)