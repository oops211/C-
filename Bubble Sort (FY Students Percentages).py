def bubble_sort(per):
    for i in range(len(per)-1):
        for j in range(len(per)-i-1):
            if per[j] > per[j+1]:
                per[j], per[j+1] = per[j+1], per[j]
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
        print("3. Sort (Bubble Sort)")
        print("4. Display Top 5 Scores")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Percentages:", per)
        elif ch == 2:
            per.sort()
            print("Sorted (Built-in):", per)
        elif ch == 3:
            per = bubble_sort(per)
            print("Sorted (Bubble Sort):", per)
        elif ch == 4:
            sorted_list = sorted(per)
            print("Top 5 Scores:", sorted_list[-5:])
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()