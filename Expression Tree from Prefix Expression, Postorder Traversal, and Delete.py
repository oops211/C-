class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in "+-*/"

def build_tree(prefix):
    stack = []
    for ch in reversed(prefix):
        node = Node(ch)
        if is_operator(ch):
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)
    return stack[-1]

def postorder_non_recursive(root):
    if not root:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    print("Postorder Traversal:", end=" ")
    while stack2:
        print(stack2.pop().value, end=" ")
    print()

def delete_tree(root):
    root = None
    print("Tree deleted successfully.")
    return root

def main():
    root = None
    while True:
        print("\nMENU")
        print("1. Build Expression Tree (from Prefix)")
        print("2. Postorder Traversal")
        print("3. Delete Tree")
        print("4. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            prefix = input("Enter prefix expression: ")
            root = build_tree(prefix)
            print("Expression Tree created successfully.")
        elif ch == 2:
            if root:
                postorder_non_recursive(root)
            else:
                print("Tree is empty.")
        elif ch == 3:
            root = delete_tree(root)
        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()