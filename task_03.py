import heapq


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float("inf"):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    visited = []

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

        visited.append(current_vertex)

        print_table(distances, visited)

    return distances


graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3},
    "C": {"A": 10, "D": 2},
    "D": {"B": 3, "C": 2, "E": 4},
    "E": {"D": 4, "H": 8},
    "F": {"G": 1},
    "G": {"F": 1, "H": 6},
    "H": {"B": 2, "C": 3, "E": 1, "G": 6},
}

dijkstra(graph, "A")
