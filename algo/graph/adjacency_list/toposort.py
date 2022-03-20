from collections import defaultdict
from graph import Graph

SHOW_INDEGREE_TEST = True

def indegree_sort(g):
    """
    Takes a graph with adjacency implementation, computes the indegree for vertices

    Then uses queue and the indegree to perform topological sort
    """
    queue = []  # track the order of dequeueing
    result = [] # used to store result
    counter = 0 # used to track how many vertices were accessed
    indegree_map = defaultdict(int) # tracks indegree for all vertices

    # populate indegree map O(VE), indegree is the number of incoming edges
    for u in g.adjList:
        for v in g.adjList[u]:
            indegree_map[v] += 1
    for u in g.adjList:
        if u not in indegree_map:
            indegree_map[u] = 0

    # append all vertices with indegree = 0
    for v in g.adjList:
        if indegree_map[v] == 0:
            queue.append(v)
    
    while queue:
        v = queue.pop(0)
        result.append(v)
        counter += 1
        
        for nb in g.adjList[v]:
            indegree_map[nb] -= 1
            if indegree_map[nb] == 0:
                queue.append(nb)
    
    if counter != g.V:
        raise Exception("Cycle detected")

    print(result)
    return result



if SHOW_INDEGREE_TEST:
    """
    Test indegreeSort implementation
    """
    g = Graph(6)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(0,3)
    g.add_edge(1,2)
    g.add_edge(1,4)
    g.add_edge(4,5)
    g.add_edge(3,5)
    g.add_edge(4,5)
    g.add_edge(3,4)
    indegree_sort(g)