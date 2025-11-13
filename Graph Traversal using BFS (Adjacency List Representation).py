from collections import deque

graph = {}

def add_edge():
    u = int(input("Enter starting node: "))
    v = int(input("Enter connected node: "))
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph
    print(f"Edge added between {u} and {v}")

def display_graph():
    print("\nAdjacency List:")
    for node, neighbors in graph.items():
        print(node, ":", neighbors)

def bfs(start):
    if start not in graph:
        print("Start node not found in graph.")
        return
    visited = set()
    queue = deque([start])
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

def main():
    while True:
        print("\nMENU")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. BFS Traversal")
        print("4. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            add_edge()
        elif ch == 2:
            display_graph()
        elif ch == 3:
            start = int(input("Enter start node: "))
            bfs(start)
        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()