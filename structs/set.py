class Set:

    def __init__(self):
        self.data = {}

    def __iter__(self):
        return self.data.__iter__()

    def __str__(self):
        return str(self.data.keys())

    def add(self, element):
         self.data[element] = None

    def remove(self, element):
        del self.data[element]

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

        for key in self:
            rezultat.add(key)
        for n in s:
            try:
                self.data[n]
                rezultat.remove(n)
            except KeyError:
                pass

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


