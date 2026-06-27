from tabulate import tabulate
import json


class Task():
    def __init__(self,task,priority):
        self.task = task
        self.priority = priority
        self.done = "Incomplete"
    
    def to_list(self):
        return [self.task,self.priority,self.done]
    
    def to_dict(self):
        return {
            "task" : self.task,
            "priority" : self.priority,
            "done" : self.done
        }
    

class Habit():
    def __init__(self,habit,frequency,target):
        self.habit = habit
        self.frequency = frequency
        self.target = target
    
    def to_list(self):
        return [self.habit,self.frequency,self.target]
    
    def to_dict(self):
        return {
            "habit" : self.habit,
            "frequency" : self.frequency,
            "target" : self.target
        }


try:
    with open("data.json", "r") as file:
        data = json.load(file)
        temp = []
        for t in data["task"]:
            task = Task(t["task"],t["priority"])
            task.done = t["done"]
            temp.append(task)
        data["task"] = temp
        temp = []
        for h in data["habit"]:
            habit = Habit(h["habit"],h["frequency"],h["target"])
            temp.append(habit)
        data["habit"] = temp
        '''
        temp = []
        for n in data["note"]:
            note = Task(n["title"],n["note"])
            temp.append(note)
        data["note"] = temp
        '''

except FileNotFoundError:
    data = {
        "task":[],
        "habit":[],
        "note":[],
        "log":[]
    }


def main():
    while True:
        print("Menu\n1. Tasks\n2. Habits\n3. Notes\n4. Focus Sessions\n5. Stats\n6. Exit")
        main_menu_choice = input("Choice: ")
        print()
        match main_menu_choice:
            case "1":
                tasks = data["task"]
                while True:
                    print(tabulate([task.to_list() for task in tasks],headers =["Task","Priority","Completion"],tablefmt="fancy_grid"))
                    print()
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Mark Incomplete\n4. Remove Completed\n5. Exit")
                    task_menu_choice = input("Choice: ")
                    match task_menu_choice:
                        case "1":
                            add_task(input("Task: "),input("Priority: "),tasks)
                        case "2":
                            mark_task(int(input("Task Number: ")),tasks)
                        case "3":
                            unmark_task(int(input("Task Number: ")),tasks)
                        case "4":
                            tasks = remove_marked(tasks)
                        case "5":
                            print()
                            break
                        case _:
                            print("Invalid Input")
                    print()
                    data["task"] = tasks

            case "2":
                habits = data["habit"]
                while True:
                    print(tabulate([habit.to_list() for habit in habits],headers =["Habit","Frequency","Target"],tablefmt="fancy_grid"))
                    print()
                    print("Habits Menu\n1. Add Habit\n2. Remove Habit\n3. Exit")
                    habit_menu_choice = input("Choice: ")
                    match habit_menu_choice:
                        case "1":
                            add_habit(input("Habit: "),input("Frequency: "),input("Target: "),habits)
                        case "2":
                            remove_habit(int(input("Task Number: ")),habits)
                        case "3":
                            print()
                            break
                        case _:
                            print("Invalid Input")
                    print()
                    data["habit"] = habits

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

    data["task"] = [task.to_dict() for task in tasks]
    data["habit"] = [habit.to_dict() for habit in habits]
    with open("data.json", "w") as file:
        json.dump(data,file,indent=4)
        file.close()


#Task functions
def add_task(task,priority,tasks):
    tasks.append(Task(task,priority))

def mark_task(i,tasks):
    tasks[i-1].done = "Complete"

def unmark_task(i,tasks):
    tasks[i-1].done = "Incomplete"

def remove_marked(tasks):
    return [task for task in tasks if task.done != "Complete"]

#Habit functions
def add_habit(habit,frequency,target,habits):
    habits.append(Habit(habit,frequency,target))

def remove_habit(i,habits):
    del habits[i-1]


if __name__ == "__main__":
    main()