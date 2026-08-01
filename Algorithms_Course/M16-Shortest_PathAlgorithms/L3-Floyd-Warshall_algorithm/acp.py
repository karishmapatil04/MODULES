# Count all possible paths between two vertices using DFS

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # DFS function to count paths
    def count_paths_util(self, u, d, visited):
        if u == d:
            return 1

        visited[u] = True
        count = 0

        for neighbor in self.graph[u]:
            if not visited[neighbor]:
                count += self.count_paths_util(neighbor, d, visited)

        visited[u] = False
        return count

    # Function to count all paths
    def count_paths(self, s, d, vertices):
        visited = [False] * vertices
        return self.count_paths_util(s, d, visited)


# Main Program
g = Graph()

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

print("Enter the edges (source destination):")
for _ in range(edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

source = int(input("Enter source vertex: "))
destination = int(input("Enter destination vertex: "))

result = g.count_paths(source, destination, vertices)

print("Total possible paths:", result)