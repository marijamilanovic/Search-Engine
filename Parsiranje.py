from Parser import  *
import os
from Trie import TrieNode, add, searching

def parsiraj():
    root_dir = 'C:\\Users\\MASHA\\Desktop\\FAKS\\OISiSI\\MojDrugiProjekatMasha\\Projekat2\\test-skup\\python-2.7.7-docs-html'
    parser = Parser()
    dictionary = {}                                                                 # KLJUC = linkovi, VREDNOST = trie svih reci
    root = TrieNode(root_dir)                                         # DA LI TRIE ZA SVE ILI ZA SVAKI LINK POSEBNO?
    for dir_path, dir_names, files in os.walk(root_dir):                            # "walking the tree"
        for file in files:
            if file.endswith(".html"):
                #root = TrieNode('')
                path = os.path.abspath(dir_path + os.sep + file).lower()            # path.abspath -> Return a normalized absolutized version of the pathname path
                words = parser.parse(path)[1]                                       # os.sep -> The character used by the operating system to separate pathname components
                links = parser.parse(path)[0]                                       # MILICE TREBA TI ZA GRAF
                for rec in words:
                    add(root, rec.lower())
                dictionary[path] = root
                print(dictionary[path])
    return root


def parsirajZadato(root_dir = str):
    parser = Parser()
    dictionary = {}
    root = TrieNode('')
    for dir_path, dir_names, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                #root = TrieNode('')
                path = os.path.abspath(dir_path + os.sep + file).lower()
                words = parser.parse(path)[1]
                links = parser.parse(path)[0]
                for rec in words:
                    add(root, rec.lower())
                dictionary[path] = root
                print(dictionary[path])


def parsirajQ(root_dir, inWord):                                    # IZMENITI - MOZDA UNUTAR TRIE DA PRETRAZUJE
    parser = Parser()
    counter = 0
    br = 0
    recnik={}
    dictionary = {}
    root = TrieNode('')
    for dir_path, dir_names, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                #root = TrieNode('')
                path = os.path.abspath(dir_path + os.sep + file).lower()
                words = parser.parse(path)[1]
                pri = ispisNazivaFajla(path)
                print(pri)
                br = 0
                for rec in words:
                    add(root, rec.lower())
                dictionary[path] = root
                print(dictionary[path])
                for rec in words:
                    if rec.lower() == inWord.lower():
                        counter += 1
                        br += 1
                recnik[path] = br
                print(" --->  " + str(recnik[path]))
                print("")
    print("BROJ PONAVLJANJA:  " + str(counter))
    if(counter == 0):
        print("Data rec ne postoji!")
    return recnik



def ispisNazivaFajla(file):
    a = file.split("\\")
    return a[-1][:-5]

