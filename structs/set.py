class Set:

    def __init__(self):
        self.data = {}

    def __iter__(self):
        return self.data.__iter__()

    def add(self, element):
         self.data[element] = None

    def union(self, *args):
        rezultat = Set()

        for i in self.data:
            rezultat.add(i)

        for i in args:
            for j in i:
                rezultat.add(j)

        return rezultat

    def difference(self, s):
        rezultat = Set()

        for key in s:
            try:
                self.data[key]
            except KeyError:
                rezultat.add(key)

        return rezultat

    def intersection(self, s):
        rezultat = Set()

        for key in s:
            try:
                self.data[key]
                rezultat.add(key)
            except KeyError:
                pass

        return rezultat


