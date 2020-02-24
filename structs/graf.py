class Cvor:
    def __init__(self, putanja):
        self.putanja = putanja
        self.linkovi = []

    def set_linkove(self, linkovi):
        self.linkovi = linkovi

    def __repr__(self):
        return f"Cvor(path:{self.putanja}, links:{self.linkovi}"

    def __str__(self):
        return f"Cvor(path:{self.putanja}, links:{self.linkovi}"


class Graf:
    def __init__(self):
        self.cvorovi = {}

    def napravi_cvorove(self, x=None):
        self.cvorovi[x.putanja] = x

        for kljuc in self.cvorovi.keys():
            if self.cvorovi[kljuc] == x:
                continue
            for link in self.cvorovi[kljuc].linkovi:
                if x.putanja == link:
                    self.cvorovi[kljuc].ivice.append(x)
            for link in x.linkovi:
                if link == self.cvorovi[kljuc].putanja:
                    x.ivice.append(self.cvorovi[kljuc])

    def print_graf(self):
        for kljuc in self.cvorovi.keys():
            print(self.cvorovi[kljuc])