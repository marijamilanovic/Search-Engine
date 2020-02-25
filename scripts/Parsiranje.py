import time
import os

from modules.Parser import  *
from structs.Trie import *
from structs.graf import Graf


def get_html_fajlove(putanja):
    lista_svih = os.listdir(putanja)
    lista_fajlova = list()
    for f in lista_svih:
        file_putanja = os.path.join(putanja, f)
        if os.path.isfile(file_putanja):
            if f.endswith('.html'):
                lista_fajlova.append(file_putanja)
        elif os.path.isdir(file_putanja):
            lista_fajlova = lista_fajlova + get_html_fajlove(file_putanja)
    return lista_fajlova


def parsiraj_html(putanja):
    dictionary = {}
    graf = Graf()
    parser = Parser()
    root = TrieNode(putanja)
    html_putanja = get_html_fajlove(putanja)
    lista_veza = list()
    print("Trenutno se HTML fajlovi parsiraju...")
    start_time = time.time()
    for html in html_putanja:
        linkovi, reci = parser.parse(html)
        #add(root, reci)
        for rec in reci:
            add(root, rec.lower(), html)
        dictionary[html] = root

        for link in linkovi:
            lista_veza.append((html, link))

    all_vertex = set()
    for e in lista_veza:
        all_vertex.add(e[0])
        all_vertex.add(e[1])

    for v in all_vertex:
        graf.insert_vertex(v)

    for e in lista_veza:
        src = e[0]
        dest = e[1]

        graf.insert_edge(src, dest)

    print("\n\nUcitavanje u graph i trie za: %s seconds." % (time.time() - start_time))

    return dictionary, graf



def newDictionary(inWord, dictionary):                                      # KLJUC - putanja, VREDNOST - trie
    newDict = {}
    current = 0
    brStr = 0
    root = None
    for key, value in dictionary.items():
        #print("kljuc  " + str(key))
        #print("vrednost  " + str(value))
        if int(searching(value, inWord)[1]) != 0:
            root, current, newDict = searching(value, inWord)               # KLJUC - putanja, VREDNOST - broj ponavljanja
    print("BROJ PONAVLJANJA --> " + str(current))
    if (current == 0):
        print("Data rec ne postoji!")
    return  newDict, current


def ispisNazivaFajla(file):
     a = file.split("\\")
     return a[-1][:-5]

