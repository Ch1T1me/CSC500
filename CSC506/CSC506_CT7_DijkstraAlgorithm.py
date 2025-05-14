import heapq

# Simulated road map as a graph (dictionary)
graph = {
    'Warehouse': {'A': 4, 'B': 2},
    'A': {'C': 3, 'D': 2},
    'B': {'A': 1, 'D': 4},
    'C': {'Destination': 2},
    'D': {'C': 1, 'Destination': 5},
    'Destination': {}
}

def dijkstra(graph, start, end):
    queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return distances[end], path

# Run simulation from Warehouse to Destination
shortest_distance, shortest_path = dijkstra(graph, 'Warehouse', 'Destination')
(shortest_distance, shortest_path)
print(f"Shortest distance: {shortest_distance}")
print(f"Shortest path: {shortest_path}")