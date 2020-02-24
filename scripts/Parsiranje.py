import time
import os

from modules.Parser import  *
from structs.Trie import TrieNode, add, searching
from structs.graf import Graf, Cvor


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
    lista_linkova = []
    lista_reci = []
    trie = TrieNode()
    graf = Graf()
    parser = Parser()
    root = TrieNode(putanja)
    html_putanja = get_html_fajlove(putanja)
    for fajl in html_putanja:
        file_absolute_putanja = f"{os.path.abspath(os.path.dirname(putanja))}/{fajl}"
        linkovi, reci = parser.parse(fajl)
        add(root, reci)
        c = Cvor(file_absolute_putanja)
        c.set_linkove(linkovi)
        graf.napravi_cvorove(c)
    #graf.print_graf()

    return root, graf

# def parsiraj():
#     root_dir = 'C:\\Us' \
#                'ers\\MASHA\\Desktop\\FAKS\\OISiSI\\MojDrugiProjekatMasha\\Projekat2\\test-skup\\python-2.7.7-docs-html'
#     dictionary = {}                                                                     # KLJUC = linkovi, VREDNOST = trie svih reci
#     if (os.path.exists(root_dir)):
#         parser = Parser()
#         root = TrieNode(root_dir)
#         print("Trenutno se HTML fajlovi parsiraju...")
#         print("Ovo su isparsirani fajlovi: ")
#         for dir_path, dir_names, files in os.walk(root_dir):                            # "walking the tree"
#             for file in files:
#                 if file.endswith(".html"):
#                     #root = TrieNode('')
#                     path = os.path.abspath(dir_path + os.sep + file).lower()            # path.abspath -> Return a normalized absolutized version of the pathname path
#                     words = parser.parse(path)[1]                                       # os.sep -> The character used by the operating system to separate pathname components
#                     links = parser.parse(path)[0]                                       # MILICE TREBA TI ZA GRAF
#                     pri = ispisNazivaFajla(path)
#                     print(pri)
#                     for rec in words:
#                         add(root, rec.lower())
#                     dictionary[path] = root
#                     #print(dictionary[path])
#         print("")
#         print("--> Uspesno isparsirani fajlovi...")
#     else:
#         print("Dati link ka folderu nije validan...")
#         return  None
#     return dictionary
#
#
# def parsirajZadato(root_dir = str):
#     parser = Parser()
#     dictionary = {}
#     root = TrieNode('')
#     print("Trenutno se HTML fajlovi parsiraju...")
#     print("Ovo su isparsirani fajlovi: ")
#     for dir_path, dir_names, files in os.walk(root_dir):
#         for file in files:
#             if file.endswith(".html"):
#                 #root = TrieNode('')
#                 path = os.path.abspath(dir_path + os.sep + file).lower()
#                 words = parser.parse(path)[1]
#                 links = parser.parse(path)[0]
#                 pri = ispisNazivaFajla(path)
#                 print(pri)
#                 for rec in words:
#                     add(root, rec.lower())
#                 dictionary[path] = root
#                 #print(dictionary[path])
#     print("")
#     print("--> Uspesno isparsirani fajlovi...")
#     return dictionary
#
#
#
# def parsirajQ(root_dir, inWord):                                # radi, ali bolje je preko trie - NE KORISTIM, mozda zatreba
#     parser = Parser()
#     counter = 0
#     br = 0
#     recnik={}
#     dictionary = {}
#     root = TrieNode('')
#     for dir_path, dir_names, files in os.walk(root_dir):
#         for file in files:
#             if file.endswith(".html"):
#                 #root = TrieNode('')
#                 path = os.path.abspath(dir_path + os.sep + file).lower()
#                 words = parser.parse(path)[1]
#                 pri = ispisNazivaFajla(path)
#                 print(pri)
#                 br = 0
#                 for rec in words:                            # skroz nebitno ovde
#                     add(root, rec.lower())
#                 dictionary[path] = root
#                 print(dictionary[path])
#                 for rec in words:
#                     if rec.lower() == inWord.lower():
#                         counter += 1
#                         br += 1
#                 recnik[path] = br
#                 print(" --->  " + str(recnik[path]))
#                 print("")
#     print("BROJ PONAVLJANJA:  " + str(counter))
#     if(counter == 0):
#         print("Data rec ne postoji!")
#     return recnik
#
#
#
def newDictionary(inWord, dictionary):                              # KLJUC - putanja, VREDNOST - trie
    newDict = {}
    current = 0
    brStr = 0
    for key, value in dictionary.items():
        #print("kljuc  " + str(key))
        #print("vrednost  " + str(value))
        if int(searching(value, inWord)[1]) != 0:
            root, current, newDict = searching(value, inWord)               # KLJUC - putanja, VREDNOST - broj ponavljanja
    print("BROJ PONAVLJANJA --> " + str(current))
    if (current == 0):
        print("Data rec ne postoji!")

    return  newDict, current
#
#
#
def ispisNazivaFajla(file):
     a = file.split("\\")
     return a[-1][:-5]

