# Hash Table using Division Method with Chaining
size = 10
table = [[] for _ in range(size)]

def insert():
    key = int(input("Enter key: "))
    value = input("Enter value: ")
    index = key % size
    table[index].append((key, value))
    print(f"Inserted ({key}, {value}) at index {index}")

def search():
    key = int(input("Enter key to search: "))
    index = key % size
    for k, v in table[index]:
        if k == key:
            print(f"Found: Key={k}, Value={v}")
            return
    print("Key not found.")

def delete():
    key = int(input("Enter key to delete: "))
    index = key % size
    for pair in table[index]:
        if pair[0] == key:
            table[index].remove(pair)
            print("Key deleted.")
            return
    print("Key not found.")

def display():
    print("\nHash Table:")
    for i in range(size):
        print(i, ":", table[i])

def main():
    while True:
        print("\nMENU")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
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