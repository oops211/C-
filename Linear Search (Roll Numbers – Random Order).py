def linear_search(roll, key):
    for i in range(len(roll)):
        if roll[i] == key:
            return i
    return -1

def main():
    n = int(input("Enter number of students: "))
    roll = []
    for i in range(n):
        roll.append(int(input(f"Enter roll number {i+1}: ")))

    while True:
        print("\nMENU")
        print("1. Display Roll Numbers")
        print("2. Search Roll Number (Linear Search)")
        print("3. Sort Roll Numbers (Built-in)")
        print("4. Sort Roll Numbers (Selection Sort)")
        print("5. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            print("Roll Numbers:", roll)
        elif ch == 2:
            key = int(input("Enter roll number to search: "))
            pos = linear_search(roll, key)
            print("Student attended." if pos != -1 else "Student not attended.")
        elif ch == 3:
            print("Sorted Roll Numbers (Built-in):", sorted(roll))
        elif ch == 4:
            arr = roll[:]
            for i in range(len(arr)):
                min_i = i
                for j in range(i+1, len(arr)):
                    if arr[j] < arr[min_i]:
                        min_i = j
                arr[i], arr[min_i] = arr[min_i], arr[i]
            print("Sorted Roll Numbers (Selection Sort):", arr)
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()