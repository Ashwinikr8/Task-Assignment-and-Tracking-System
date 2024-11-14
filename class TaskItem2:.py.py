class TaskItem:
    def __init__(self, title, details, assignee):
        self.title = title
        self.details = details
        self.assignee = assignee
        self.status = 'Not Started'

    def __str__(self):
        return f"[Task: {self.title} | Details: {self.details} | Assigned To: {self.assignee} | Status: {self.status}]"


class TaskTracker:
    def __init__(self):
        self.task_list = []

    def create_task(self, title, details, assignee):
        task = TaskItem(title, details, assignee)
        self.task_list.append(task)
        print(f"New task '{title}' has been successfully created!")

    def display_tasks(self):
        if not self.task_list:
            print("There are currently no tasks available.")
            return
        print("\n--- Task List ---")
        for i, task in enumerate(self.task_list, start=1):
            print(f"{i}. {task}")
        print("-----------------")

    def change_task_status(self, index, status_update):
        if 0 <= index < len(self.task_list):
            self.task_list[index].status = status_update
            print(f"The status of '{self.task_list[index].title}' has been updated to '{status_update}'.")
        else:
            print("Task index is out of range. Please try again.")

    def remove_task(self, index):
        if 0 <= index < len(self.task_list):
            removed_task = self.task_list.pop(index)
            print(f"Task '{removed_task.title}' has been removed from the list.")
        else:
            print("Invalid task index. Unable to delete the task.")

    def launch(self):
        while True:
            print("\n=== Task Tracking System ===")
            print("1. Create a New Task")
            print("2. Show All Tasks")
            print("3. Update Task Status")
            print("4. Delete a Task")
            print("5. Exit System")

            choice = input("Select an action: ")
            if choice == '1':
                title = input("Enter task title: ")
                details = input("Enter task details: ")
                assignee = input("Who will be assigned this task? ")
                self.create_task(title, details, assignee)
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                index = int(input("Enter the task number to update: ")) - 1
                status_update = input("Enter new status (Not Started/In Progress/Completed): ")
                self.change_task_status(index, status_update)
            elif choice == '4':
                index = int(input("Enter the task number to delete: ")) - 1
                self.remove_task(index)
            elif choice == '5':
                print("Exiting the Task Tracking System. Have a great day!")
                break
            else:
                print("Invalid selection. Please choose a valid option.")


if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.launch()