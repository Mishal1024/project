from tabulate import tabulate

class Task():
    def __init__(self,task,priority):
        self.task = task
        self.priority = priority
        self.done = "Incomplete"
    
    def to_list(self):
        return [self.task,self.priority,self.done]
    
try:
    data = open("data.json","r")
except FileNotFoundError:
    data = open("data.json","w")
    data.write('{\n\t"task":["Task","Priority","Completion"]\n\t"habit":\n\t"note":\n}')
    data.close()


def main():
    while True:
        print("Menu\n1. Tasks\n2. Habits\n3. Notes\n4. Focus Sessions\n5. Stats\n6. Exit")
        main_menu_choice = input("Choice: ")
        print()
        match main_menu_choice:
            case "1":
                tasks = [["Task","Priority","Completion"]]
                while True:
                    print(tabulate(tasks,headers = "firstrow",tablefmt="grid"))
                    print()
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Remove Completed\n4. Exit")
                    task_menu_choice = input("Choice: ")
                    match task_menu_choice:
                        case "1":
                            task = input("Task: ")
                            priority = input("Priority: ")
                            tasks.append(Task(task,priority).to_list())
                        case "2":
                            tasks[int(input("Task Number: "))][2] = "Complete"
                        case "3":
                            tasks = [task for task in tasks if task[2] != "Complete"]
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