from collections import deque

events = deque()

def add_event(e):
    events.append(e)
    print(f"Event '{e}' added.")

def process_event():
    if events:
        print("Processed:", events.popleft())
    else:
        print("No events to process.")

def display_events():
    if events:
        print("Pending Events:", list(events))
    else:
        print("No pending events.")

def cancel_event(e):
    if e in events:
        events.remove(e)
        print(f"Event '{e}' cancelled.")
    else:
        print("Event not found.")

def main():
    while True:
        print("\nMENU")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel an Event")
        print("5. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            e = input("Enter event name: ")
            add_event(e)
        elif ch == 2:
            process_event()
        elif ch == 3:
            display_events()
        elif ch == 4:
            e = input("Enter event name to cancel: ")
            cancel_event(e)
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()