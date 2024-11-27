#28. Implementera en algoritm för Dijkstra's kortaste väg.

import heapq

def dijkstra(graph, start):
    # Initiera avståndstabell med oändligt stora värden
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Prioritetskö (min-heap) för att hantera noder att utforska
    priority_queue = [(0, start)]  # (avstånd, nod)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Om vi redan har en kortare väg till noden, hoppa över
        if current_distance > distances[current_node]:
            continue
        
        # Utforska grannarna
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Om vi hittar en kortare väg, uppdatera avståndet
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Exempel på användning
if __name__ == "__main__":
    # Exempelgraf som en oriktad graf med vikter
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"Kortaste avstånd från {start_node}: {shortest_distances}")
