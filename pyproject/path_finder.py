def shortest_path(graph, start, end):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    path = {node: [] for node in graph}
    path[start] = [start]

    visited = []

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distance[node] < distance[min_node]:
                    min_node = node

        visited.append(min_node)

        for neighbor, weight in graph[min_node].items():
            new_dist = distance[min_node] + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                path[neighbor] = path[min_node] + [neighbor]

    return path[end], distance[end]


# -------- Graph Input --------
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = {}
    edges = int(input(f"How many neighbors for {node} ? "))

    for _ in range(edges):
        neighbor = input("Enter neighbor: ")
        weight = int(input("Enter distance: "))
        graph[node][neighbor] = weight

# -------- Run --------
start = input("Enter start node: ")
end = input("Enter end node: ")

p, d = shortest_path(graph, start, end)

print("\n Shortest Path:", " → ".join(p))
print(" Total Distance:", d)