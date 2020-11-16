# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:56:52 2020

@author: Harry
"""

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def edges(self):
        return self.findedges()
    
    def addedge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
    def getvertices(self):
        return list(self.gdict.keys())
    
    def addvertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }
g = graph(graph_elements)
g.addedge({'a','e'})
g.addedge({'a','c'})
g.addvertex("f")
print(g.edges())
print(g.getvertices())
