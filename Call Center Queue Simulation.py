from collections import deque

calls = deque()

def add_call():
    cid = input("Enter Customer ID: ")
    ctime = int(input("Enter Call Time (in minutes): "))
    calls.append((cid, ctime))
    print("Call added to queue.")

def answer_call():
    if calls:
        cid, ctime = calls.popleft()
        print(f"Answered call from Customer {cid} (Duration: {ctime} mins).")
    else:
        print("No calls to answer.")

def view_queue():
    if calls:
        print("Current Call Queue:")
        for c in calls:
            print(f"Customer ID: {c[0]}, Call Time: {c[1]} mins")
    else:
        print("Queue is empty.")

def is_empty():
    print("Queue Empty" if not calls else "Queue Not Empty")

def main():
    while True:
        print("\nMENU")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Check if Queue is Empty")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            add_call()
        elif ch == 2:
            answer_call()
        elif ch == 3:
            view_queue()
        elif ch == 4:
            is_empty()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()