size = 10
table = [None] * size

def insert():
    key = int(input("Enter key: "))
    index = key % size
    start = index
    while table[index] is not None:
        index = (index + 1) % size
        if index == start:
            print("Hash table full!")
            return
    table[index] = key
    print(f"Inserted key {key} at index {index}")

def search():
    key = int(input("Enter key to search: "))
    index = key % size
    start = index
    while table[index] is not None:
        if table[index] == key:
            print(f"Key {key} found at index {index}")
            return
        index = (index + 1) % size
        if index == start:
            break
    print("Key not found.")

def delete():
    key = int(input("Enter key to delete: "))
    index = key % size
    start = index
    while table[index] is not None:
        if table[index] == key:
            table[index] = None
            print(f"Key {key} deleted.")
            return
        index = (index + 1) % size
        if index == start:
            break
    print("Key not found.")

def display():
    print("\nHash Table:")
    for i in range(size):
        print(i, ":", table[i])

def main():
    while True:
        print("\nMENU")
        print("1. Insert Key")
        print("2. Search Key")
        print("3. Delete Key")
        print("4. Display Table")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            search()
        elif ch == 3:
            delete()
        elif ch == 4:
            display()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()