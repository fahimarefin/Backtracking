from collections import defaultdict

node, edge = map(int, input().split())


def isSafe(graph, v, color, c):
    for i in range(1, len(graph)):

        if graph[v][i] and c == color[i]:
            return False

    return True


def graph_color(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(0, m):
        if isSafe(graph, v, color, c):
            color[v] = c
            if graph_color(graph, m, color, v + 1):
                return True

            color[v] = -1

    return False


def printSolution(color):
    for i in range(1, node+1):
        print(color[i])


def initializeGraphColoring(graph, m):
    color = defaultdict(list)
    if not graph_color(graph, m, color, 1):
        print("No")
        return

    printSolution(color)


if __name__ == "__main__":

    graph = [[0 for i in range(0, node + 1)] for j in range(0, node + 1)]

    for i in range(0, edge):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1

    k = int(input())

    initializeGraphColoring(graph, k)
