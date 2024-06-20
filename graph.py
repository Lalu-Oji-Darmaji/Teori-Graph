class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict

    def getVertex(self):
        return list(self.gdict.keys())
    def getEdges(self):
        edges=[]
        for v in self.gdict:
            for e in self.gdict[v]:
                if {e,v} not in edges:
                    edges.append({e,v})
        return edges

    def addVertex(self,v):
        if v not in self.gdict:
            self.gdict[v]=[]

    def addEdges(self,e):
        (v1,v2)=e
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1]=[v2]
        if v2 in self.gdict:
            self.gdict[v2].append(v1)
        else:
            self.gdict[v2]=[v1]
        

graph1 = {"a" : ["b","c"],
          "b" : ["a","d"],
          "c" : ["a","d"],
          "d" : ["e"],    
          "e" : ["d"]
          }

tampilan="%-20s : %s"
g=graph(graph1)
print(tampilan%("Vertex awal",g.getVertex()))
print(tampilan%("Edge awal",g.getEdges()))
g.addVertex("f")
print(tampilan%("Vertex tambah",g.getVertex()))
g.addEdges({"f","c"})
print(tampilan%("Edge tambah",g.getEdges()))
