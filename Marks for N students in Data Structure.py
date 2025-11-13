from statistics import mode

def average(marks):
    valid = [m for m in marks if m > 0]
    return sum(valid) / len(valid) if valid else 0

def high_low(marks):
    valid = [m for m in marks if m > 0]
    return (max(valid), min(valid)) if valid else (0, 0)

def absent(marks):
    return marks.count(0)

def frequent(marks):
    valid = [m for m in marks if m > 0]
    return mode(valid) if valid else None

def main():
    n = int(input("Enter number of students: "))
    marks = []
    for i in range(n):
        m = int(input(f"Enter marks of student {i+1} (0 for absent): "))
        marks.append(m)

    while True:
        print("\nMENU\n1.Average\n2.Highest & Lowest\n3.Absent Count\n4.Most Frequent\n5.Sort (Built-in)\n6.Sort (Selection)\n7.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            print("Average Score:", average(marks))
        elif ch == 2:
            h, l = high_low(marks)
            print("Highest:", h, "Lowest:", l)
        elif ch == 3:
            print("Absent Count:", absent(marks))
        elif ch == 4:
            print("Most Frequent Mark:", frequent(marks))
        elif ch == 5:
            print("Sorted (Built-in):", sorted([m for m in marks if m > 0]))
        elif ch == 6:
            arr = [m for m in marks if m > 0]
            for i in range(len(arr)):
                min_i = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[min_i]:
                        min_i = j
                arr[i], arr[min_i] = arr[min_i], arr[i]
            print("Sorted (Selection):", arr)
        elif ch == 7:
            break
        else:
            print("Invalid choice")

main()