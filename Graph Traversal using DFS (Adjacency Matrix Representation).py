def create_graph():
    n = int(input("Enter number of vertices: "))
    matrix = [[0] * n for _ in range(n)]
    e = int(input("Enter number of edges: "))
    for _ in range(e):
        u = int(input("Enter starting vertex: "))
        v = int(input("Enter ending vertex: "))
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected
    return matrix, n

def display_graph(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

def dfs(matrix, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited)

def main():
    matrix, n = create_graph()
    while True:
        print("\nMENU")
        print("1. Display Graph")
        print("2. Perform DFS Traversal")
        print("3. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            display_graph(matrix)
        elif ch == 2:
            start = int(input("Enter start vertex: "))
            visited = [False] * n
            print("DFS Traversal:", end=" ")
            dfs(matrix, start, visited)
            print()
        elif ch == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()