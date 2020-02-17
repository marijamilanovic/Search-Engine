
class TrieNode(object):

    def __init__(self, char=str):
        self.char = char
        self.children = []                                      # lista reci
        self.leaf = False                                       # da l je poslednji
        self.counter = 1


def add(root, word=str):
    node = root
    for char in word:
        found_child = False
        for child in node.children:                             # trazi karakter u trenutnom cvoru
            if child.char == char:                              # ako smo nasli
                child.counter += 1                              # povecaj brojac
                node = child                                    # vezi cvor i dete
                found_child = True
                break
        if not found_child:                                     # ako nismo nasli, treba napraviti
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node                                     # vezi cvor i dete
    node.leaf = True                                            # kraj reci - list


def searching(root, search=str):
    node = root
    if not root.children:                                       # ako root nema dece -> false
        return False, 0
    for char in search:
        char_not_found = True
        for child in node.children:                             # pretrazi decu trenutnog cvora
            if child.char == char:                              # ako smo nasli
                char_not_found = False
                node = child
                break
        if char_not_found:                                      # ako nismo nasli
            return False, 0
    return True, node.counter                                   # nasli prefiks znaci vrati TRUE i brojac poklapanja


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, 'masalaa')
    add(root, 'mas')
    add(root, 'tttt')

    print(searching(root, 'ma'))
    print(searching(root, 'masalaaaa'))
    print(searching(root, 'maa'))
    print(searching(root, 'masal'))
    print(searching(root, 'tata'))
    print(searching(root, 'tttt'))