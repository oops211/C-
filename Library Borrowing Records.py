from statistics import mode

def avg(d):
    return sum(d.values()) / len(d)

def high_low(d):
    return max(d, key=d.get), min(d, key=d.get)

def zero_count(d):
    return sum(1 for x in d.values() if x == 0)

def frequent(d):
    return mode(d.values())

def main():
    n = int(input("Enter number of books: "))
    books = {}
    for i in range(n):
        name = input(f"Enter book {i+1} name: ")
        count = int(input(f"Enter borrow count for {name}: "))
        books[name] = count

    while True:
        print("\nMENU\n1. Average\n2. Highest & Lowest\n3. Zero Borrow\n4. Most Frequent\n5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            print("Average borrow:", avg(books))
        elif ch == 2:
            h, l = high_low(books)
            print("Highest:", h, "Lowest:", l)
        elif ch == 3:
            print("Zero Borrow:", zero_count(books))
        elif ch == 4:
            print("Most Frequent Borrow Count:", frequent(books))
        elif ch == 5:
            break
        else:
            print("Invalid choice")

main()
