#23. **Implementera en algoritm för att hitta alla starkt sammanhängande komponenter i en graf.**
from collections import defaultdict

class TarjanSCC:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = defaultdict(list)
        self.index = 0
        self.stack = []
        self.indices = [-1] * num_nodes
        self.lowlink = [-1] * num_nodes
        self.on_stack = [False] * num_nodes
        self.sccs = []

    def add_edge(self, u, v):
        """Lägger till en riktad kant från u till v."""
        self.graph[u].append(v)

    def strong_connect(self, node):
        """DFS-baserad rekursiv funktion för att identifiera SCCs."""
        self.indices[node] = self.index
        self.lowlink[node] = self.index
        self.index += 1
        self.stack.append(node)
        self.on_stack[node] = True

        # Utforska alla grannar
        for neighbor in self.graph[node]:
            if self.indices[neighbor] == -1:  # Om noden inte har besökts
                self.strong_connect(neighbor)
                self.lowlink[node] = min(self.lowlink[node], self.lowlink[neighbor])
            elif self.on_stack[neighbor]:  # Om den är i stacken, är den en del av en SCC
                self.lowlink[node] = min(self.lowlink[node], self.indices[neighbor])

        # Om noden är en rot i en SCC
        if self.lowlink[node] == self.indices[node]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == node:
                    break
            self.sccs.append(scc)

    def find_sccs(self):
        """Hittar alla SCCs i grafen."""
        for node in range(self.num_nodes):
            if self.indices[node] == -1:
                self.strong_connect(node)
        return self.sccs

# Exempelanvändning
if __name__ == "__main__":
    g = TarjanSCC(8)
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3), (6, 5), (6, 7)]
    for u, v in edges:
        g.add_edge(u, v)

    print("Starkt sammanhängande komponenter:", g.find_sccs())
