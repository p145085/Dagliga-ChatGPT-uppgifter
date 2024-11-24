#25. Implementera en grafstruktur och BFS/DFS-sökning.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Använder en oriktad graf med en defaultdict
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Lägger till en kant mellan noderna u och v."""
        self.graph[u].append(v)
        self.graph[v].append(u)  # Ta bort denna rad för en riktad graf.
    
    def bfs(self, start):
        """Utför BFS från en startnod."""
        visited = set()  # För att hålla reda på besökta noder
        queue = deque([start])  # BFS använder en kö
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Lägger till alla grannar som inte är besökta
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Utför DFS från en startnod."""
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Besök grannar
                for neighbor in self.graph[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

# Exempelanvändning
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("BFS:", g.bfs(0))  # Bör returnera [0, 1, 2, 3, 4]
    print("DFS:", g.dfs(0))  # Bör returnera [0, 1, 2, 3, 4] eller liknande beroende på kantordning
