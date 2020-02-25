class Graf(object):

    def __init__(self):
        self._incoming = {}
        self._outgoing = {}

    def insert_vertex(self, e):
        self._outgoing[e] = []
        self._incoming[e] = []

    def insert_edge(self, u, v):
        self._outgoing[u].append(v)
        self._incoming[v].append(u)

    def incoming_links(self,v):
        return self._incoming[v]