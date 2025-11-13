def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return i
    return -1

def main():
    n = int(input("Enter number of customer IDs: "))
    ids = []
    for i in range(n):
        ids.append(int(input(f"Enter ID {i+1}: ")))

    while True:
        print("\nMENU\n1. Display IDs\n2. Search ID (Linear Search)\n3. Sort IDs (Built-in)\n4. Sort IDs (Bubble Sort)\n5. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            print("Customer IDs:", ids)
        elif ch == 2:
            key = int(input("Enter ID to search: "))
            pos = linear_search(ids, key)
            print("ID Found at position" if pos != -1 else "ID Not Found")
        elif ch == 3:
            print("Sorted IDs (Built-in):", sorted(ids))
        elif ch == 4:
            arr = ids[:]
            for i in range(len(arr)-1):
                for j in range(len(arr)-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Sorted IDs (Bubble Sort):", arr)
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()