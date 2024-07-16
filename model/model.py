import warnings

import networkx as nx

from database.DAO import DAO





class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._edges = []
        self._nodes = []
        self.idMap={}
        self._choiceAlbum = None

        self._albumList = []



    def build_graph(self, d):
        self._graph.clear()

        self._albumList = DAO.getAlbumDurata(self.toMilli(d))

        self._nodes = self._albumList

        self._graph.add_nodes_from(self._nodes)
        for a in self._nodes:
            self.idMap[a.AlbumId] = a

        self._edges = DAO.getEdges(self.idMap)
        self._graph.add_edges_from(self._edges)



    def get_connected_components(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTOT = 0
        for album in conn:
            if 'durata' in self._graph.nodes[album]:
                durataTOT += self.toMin(self._graph.nodes[album]['durata'])

        return len(conn), durataTOT


    def toMilli(self, d):
        return d*60*1000

    def toMin(self, d):
        return d/1000/60




