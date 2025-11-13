def bubble_sort(sal):
    for i in range(len(sal)-1):
        for j in range(len(sal)-i-1):
            if sal[j] > sal[j+1]:
                sal[j], sal[j+1] = sal[j+1], sal[j]
    return sal

def main():
    n = int(input("Enter number of employees: "))
    sal = []
    for i in range(n):
        s = float(input(f"Enter salary of employee {i+1}: "))
        sal.append(s)

    while True:
        print("\nMENU")
        print("1. Display Salaries")
        print("2. Sort (Built-in)")
        print("3. Sort (Bubble Sort)")
        print("4. Show Top 5 Highest Salaries")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Salaries:", sal)
        elif ch == 2:
            sal.sort()
            print("Sorted (Built-in):", sal)
        elif ch == 3:
            sal = bubble_sort(sal)
            print("Sorted (Bubble Sort):", sal)
        elif ch == 4:
            sal_sorted = sorted(sal)
            print("Top 5 Salaries:", sal_sorted[-5:])
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()