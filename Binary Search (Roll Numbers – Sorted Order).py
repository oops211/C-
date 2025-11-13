def binary_search(roll, key):
    low, high = 0, len(roll) - 1
    while low <= high:
        mid = (low + high) // 2
        if roll[mid] == key:
            return mid
        elif roll[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def selection_sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

def main():
    n = int(input("Enter number of students: "))
    roll = []
    for i in range(n):
        roll.append(int(input(f"Enter roll number {i+1}: ")))

    while True:
        print("\nMENU")
        print("1. Display Roll Numbers")
        print("2. Sort Roll Numbers (Built-in)")
        print("3. Sort Roll Numbers (Selection Sort)")
        print("4. Search Roll Number (Binary Search)")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Roll Numbers:", roll)
        elif ch == 2:
            roll.sort()
            print("Sorted (Built-in):", roll)
        elif ch == 3:
            roll = selection_sort(roll)
            print("Sorted (Selection Sort):", roll)
        elif ch == 4:
            if roll != sorted(roll):
                print("Please sort the list first!")
            else:
                key = int(input("Enter roll number to search: "))
                pos = binary_search(roll, key)
                print("Student attended." if pos != -1 else "Student not attended.")
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()