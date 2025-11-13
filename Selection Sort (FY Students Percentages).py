def selection_sort(per):
    for i in range(len(per)):
        min_i = i
        for j in range(i+1, len(per)):
            if per[j] < per[min_i]:
                min_i = j
        per[i], per[min_i] = per[min_i], per[i]
    return per

def main():
    n = int(input("Enter number of students: "))
    per = []
    for i in range(n):
        p = float(input(f"Enter percentage of student {i+1}: "))
        per.append(p)

    while True:
        print("\nMENU")
        print("1. Display Percentages")
        print("2. Sort (Built-in)")
        print("3. Sort (Selection Sort)")
        print("4. Display Top 5 Scores")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Percentages:", per)
        elif ch == 2:
            per.sort()
            print("Sorted (Built-in):", per)
        elif ch == 3:
            per = selection_sort(per)
            print("Sorted (Selection Sort):", per)
        elif ch == 4:
            sorted_list = sorted(per)
            print("Top 5 Scores:", sorted_list[-5:])
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()