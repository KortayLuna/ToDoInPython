import json
from typing import List, Dict, Any


# class for main operations
class App:
    def __init__(self, tasks: list[dict[str, Any]]) -> None:
        self.tasks = tasks

    def add_task(self, date: str, task: str, done: bool = False):
        print("Adding task:", date, task, "Done:", done)
        entry = {"date": date, "task": task, "done": done}
        self.tasks.append(entry)
        App.dumpList(self)

    def remove_task(self, task: str):
        print("Removing task:", task)
        # Implement the logic to remove a task from self.tasks

    def change_task_status(self, task: str, done: bool):
        print("Changing status for task:", task, "to Done:", done)
        # Implement the logic to change the status of a task in self.tasks

    def save_to_json(self):
        print("Saving to JSON")
        # Implement the logic to save self.tasks to a JSON file

    def dumpList(self):
        with open("todos.json", "w") as f1:
            json.dump(self.tasks, f1, indent=5)


def Main():
    with open("todos.json", "r") as f1:
        todosList: List[Dict[str, Any]] = json.load(f1)

    app = App(todosList)
    while True:
        process = input("What do you want to do: ")
        method = getattr(app, process, None)

        if method:
            if process == "add_task":
                date = input("Enter date: ")
                task = input("Enter task: ")
                method(date, task)
            elif process == "remove_task":
                task = input("Enter the task to remove: ")
                method(task)
            elif process == "change_task_status":
                task = input("Enter the task to change status: ")
                done = input("Enter new status (True/False): ")
                method(task, done)
            elif process == "save_to_json":
                method()

        elif process == "quit" or "q":
            break
        else:
            print("Invalid command. Please enter a valid action.")


if __name__ == "__main__":
    Main()
