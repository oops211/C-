def binary_search(ids, key):
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bubble_sort(arr):  # For manual sorting before search
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    n = int(input("Enter number of customer IDs: "))
    ids = []
    for i in range(n):
        ids.append(int(input(f"Enter ID {i+1}: ")))

    while True:
        print("\nMENU")
        print("1. Display IDs")
        print("2. Sort IDs (Built-in)")
        print("3. Sort IDs (Bubble Sort)")
        print("4. Binary Search ID")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Customer IDs:", ids)
        elif ch == 2:
            ids.sort()
            print("Sorted IDs (Built-in):", ids)
        elif ch == 3:
            bubble_sort(ids)
            print("Sorted IDs (Bubble Sort):", ids)
        elif ch == 4:
            if ids != sorted(ids):
                print("Please sort the list first!")
            else:
                key = int(input("Enter ID to search: "))
                pos = binary_search(ids, key)
                print("ID Found at position" if pos != -1 else "ID Not Found")
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()