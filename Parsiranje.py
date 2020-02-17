from Parser import  *
import os
from Trie import TrieNode, add

def parsiraj():
    root_dir = 'C:\\Users\\MASHA\\Desktop\\FAKS\\OISiSI\\MojDrugiProjekatMasha\\Projekat2\\test-skup\\python-2.7.7-docs-html'
    parser = Parser()
    dictionary = {}                                                             # KLJUC = linkovi, VREDNOST = trie svih reci
    #print("tu je")
    for dir_path, dir_names, files in os.walk(root_dir):                        # "walking the tree"
        #print("tuuu je")
        for file in files:
            if file.endswith(".html"):
                root = TrieNode('')
                path = os.path.abspath(dir_path + os.sep + file).lower()            # path.abspath -> Return a normalized absolutized version of the pathname path
                words = parser.parse(path)[1]                                       # os.sep -> The character used by the operating system to separate pathname components
                links = parser.parse(path)[0]                                       # MILICE TREBA TI ZA GRAF
                for rec in words:
                    add(root, rec.lower())
                dictionary[path] = root
                print(dictionary[path])



def parsirajZadato(root_dir = str):
    parser = Parser()
    dictionary = {}                                                            # KLJUC = linkovi, VREDNOST = trie svih reci
    for dir_path, dir_names, files in os.walk(root_dir):                       # "walking the tree"
        for file in files:
            if file.endswith(".html"):
                root = TrieNode('')
                path = os.path.abspath(dir_path + os.sep + file).lower()            # path.abspath -> Return a normalized absolutized version of the pathname path
                words = parser.parse(path)[1]                                       # os.sep -> The character used by the operating system to separate pathname components
                links = parser.parse(path)[0]                                       # MILICE TREBA TI ZA GRAF
                for rec in words:
                    add(root, rec.lower())
                dictionary[path] = root
                print(dictionary[path])