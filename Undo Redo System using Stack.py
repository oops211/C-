undo_stack = []
redo_stack = []

def make_change(change):
    undo_stack.append(change)
    redo_stack.clear()

def undo():
    if undo_stack:
        redo_stack.append(undo_stack.pop())
        print("Undo done.")
    else:
        print("Nothing to undo.")

def redo():
    if redo_stack:
        undo_stack.append(redo_stack.pop())
        print("Redo done.")
    else:
        print("Nothing to redo.")

def display():
    print("Current Document:", undo_stack)

def main():
    while True:
        print("\nMENU")
        print("1. Make Change")
        print("2. Undo Action")
        print("3. Redo Action")
        print("4. Display Document State")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            change = input("Enter your change: ")
            make_change(change)
        elif ch == 2:
            undo()
        elif ch == 3:
            redo()
        elif ch == 4:
            display()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()