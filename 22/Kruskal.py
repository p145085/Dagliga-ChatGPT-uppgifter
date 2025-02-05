#22. **Bygg en minsta spannträd-algoritm med Kruskal’s algoritm.**
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    """
    n: antal noder
    edges: lista av (vikt, nod1, nod2)
    """
    edges.sort()  # Sortera kanterna efter vikt
    dsu = DisjointSet(n)
    mst = []
    total_weight = 0
    
    for weight, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

# Exempelanrop
graph_edges = [
    (1, 0, 1), (4, 0, 2), (3, 1, 2),
    (2, 1, 3), (5, 2, 3)
]
nodes = 4
mst, weight = kruskal(nodes, graph_edges)
print("Minimal spannträd:", mst)
print("Total vikt:", weight)