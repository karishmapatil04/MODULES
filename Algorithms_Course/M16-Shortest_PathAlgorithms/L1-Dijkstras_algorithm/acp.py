# M-Coloring Problem using Backtracking

def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c

            if graph_coloring_util(graph, m, color, v + 1):
                return True

            color[v] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False

    print("Color Assignment:")
    for i in range(n):
        print(f"Vertex {i} ---> Color {color[i]}")
    return True

# Driver Code
n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

graph_coloring(graph, m)