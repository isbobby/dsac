from collections import defaultdict

class Graph:
    """
    Adjacency list implementation, uses a default dict of lists as the underlying data structure.

    Attributes
    ----------
    self.adjList : defaultdict(list)
        A map of lists
    self.V : int    
        number of vertex
    
    Methods
    -------
    add_edge(u,v)
        adds an edge from u to v
    print()         
        prints graph
    """
    def __init__(self, v):
        self.V = v
        self.adjList = defaultdict(list)
        return
    
    def add_edge(self,u,v):
        self.adjList[u].append(v)

        if v not in self.adjList:
            self.adjList[v] = []

        return

    def print(self):
        for v in self.adjList:
            print(f"{v} ->" + str(self.adjList[v]))
        return
