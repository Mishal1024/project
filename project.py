class Task():
    def __init__(self,task,priority):
        self.task = task
        self.priority = priority
        self.done = False
    
    def __str__(self):
        return f"{self.task} ({self.priority}) - Done: {self.done}"


def main():
    while True:
        print("Menu\n1. Tasks\n2. Habits\n3. Notes\n4. Focus Sessions\n5. Stats\n6. Exit")
        c = input("Choice: ")
        print()
        match c:
            case "1":
                tasks = []
                while True:
                    print("Tasks")
                    for ptask in tasks:
                        print(ptask)
                    print()
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Remove Completed\n4. Exit")
                    t = input("Choice: ")
                    match t:
                        case "1":
                            task = input("Task: ")
                            priority = input("Priority: ")
                            task = Task(task,priority)
                            tasks.append(task)
                        case "2":
                            tasks[int(input("Task Number: "))-1].done = True
                        case "3":
                            for i in range(len(tasks)-1):
                                if tasks[i].done == True:
                                    del tasks[i]
                        case "4":
                            print()
                            break
                        case _:
                            print("Invalid Input")
                    print()
            case "2":
                print("Habits")
            case "3":
                print("Notes")
            case "4":
                print("Focus")
            case "5":
                print("stats")
            case "6":
                break
            case _:
                print("Invalid Input")
                pass
            

def add_task():
    ...


def complete_task():
    ...



if __name__ == "__main__":
    main()