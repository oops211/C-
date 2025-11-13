class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def main():
    root = None
    while True:
        print("\nMENU")
        print("1. Insert Node")
        print("2. Search Node")
        print("3. Delete Node")
        print("4. Display (Inorder)")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            key = int(input("Enter value to insert: "))
            root = insert(root, key)
        elif ch == 2:
            key = int(input("Enter value to search: "))
            print("Found!" if search(root, key) else "Not Found!")
        elif ch == 3:
            key = int(input("Enter value to delete: "))
            root = delete(root, key)
        elif ch == 4:
            print("Inorder Traversal:", end=" ")
            inorder(root)
            print()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()