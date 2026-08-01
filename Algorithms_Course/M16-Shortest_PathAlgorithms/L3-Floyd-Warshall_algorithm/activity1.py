# Number of vertices in the graph
V = 4

# Define infinity as the large number
# This value will be enough when no path exists
INF = 99999

# Solves all pair shortest path via Floyd Warshall Algorithm
def floydWarshall(graph):
    """ 
    dist[][] will be the output matrix that 
    finally have the shortest distances 
    between every pair of vertices 
    """

    # initializing the solution matrix (copy of graph)
    dist = [row[:] for row in graph]

    # Add all vertices one by one to the set of intermediate vertices.
    for k in range(V):

        # Pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the above picked source
            for j in range(V):

                # If vertex k is on the shortest path from i to j, update dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Print the solution
    printSolution(dist)


def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print("%7d" % dist[i][j], end="  ")
        print(" ")


# Driver's code
if __name__ == "__main__":
    # Initial graph (adjacency matrix)
    graph = [[0,   5,  INF, 10],
             [INF,  0,   3, INF],
             [INF, INF,  0,   1],
             [INF, INF, INF,  0]]

    floydWarshall(graph)