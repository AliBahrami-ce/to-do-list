import csv

class Task:
    def __init__(self, task, priority, comment = None):
        self.task = task
        self.priority = priority
        self.comment = comment

    def Description(self, comment):
        self.comment = comment

    def __str__(self):
        comment_display = self.comment if self.comment else "No Comment"
        return f"task= {self.task} | priority= {self.priority} | Comment= {comment_display}" 
    
class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task : Task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"{removed} removed.")
            print("-" * 50)
        else:
            print("Task not found!")
            print("-" * 50)

    def show_task(self):
        for i, tasks in enumerate(self.tasks):
            print(f"{i + 1} ---> {tasks}")

    def save_tasks(self):
        with open('tasks.csv', mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "priority", "Comment"])

            for row in self.tasks:
                writer.writerow([row.task, row.priority, row.comment or "No Comment"])
            
to_do_list = ToDo()
choice = 0

while True:
    print("1. Add new Task.")
    print("2. Remove the Task.")
    print("3. Show all Tasks.")
    print("4. Save your Tasks in csv file.")
    print("5. exit.")
    print("-" * 50)
    
    try:
        choice = int(input("Please Enter number of your choice: "))
        print("-" * 50)

        if choice == 1:
            title = input("Enter task title: ").strip()
            priority = input("Enter task priority (high/medium/low): ").strip().lower()
            comment = input("Enter comment (optional - press enter to continue...): ").strip()
            comment = comment if comment else None

            task = Task(title, priority, comment)
            to_do_list.add_task(task)
            print("Task added successfully.")
            print("-" * 50)

        elif choice == 2:
            to_do_list.show_task()

            try:
                index = int(input("Enter the task number to remove: "))
                to_do_list.remove_task(index)

            except ValueError:
                print("Please enter a valid number!")
                print("-" * 50)

        elif choice == 3:
            to_do_list.show_task()
            print("-" * 50)

        elif choice == 4:
            to_do_list.save_tasks()
            print("Saved.")
            print("-" * 50)


        elif choice == 5:
            break

        else:
            print("Invalid choice! Please select a number between 1-5.\n")
            print("-" * 50)
    
    except ValueError:
        print("Please enter a valid number!\n")
        print("-" * 50)

