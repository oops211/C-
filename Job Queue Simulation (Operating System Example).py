from collections import deque

jobs = deque()

def add_job():
    job = input("Enter job name: ")
    jobs.append(job)
    print(f"Job '{job}' added to queue.")

def delete_job():
    if jobs:
        print(f"Deleted job: {jobs.popleft()}")
    else:
        print("No jobs to delete.")

def display_jobs():
    if jobs:
        print("Current Job Queue:", list(jobs))
    else:
        print("Job Queue is empty.")

def main():
    while True:
        print("\nMENU")
        print("1. Add Job")
        print("2. Delete Job")
        print("3. Display Job Queue")
        print("4. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            add_job()
        elif ch == 2:
            delete_job()
        elif ch == 3:
            display_jobs()
        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()