from tabulate import tabulate
import json
from datetime import datetime
from pyfiglet import Figlet
import os
import time



class Task:
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
    

class Habit:
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
    

class Note:
    def __init__(self,title,content):
        self.title = title
        self.content = content
    
    def to_list(self):
        return [self.title,self.content]
    
    def to_dict(self):
        return {
            "title" : self.title,
            "content" : self.content
        }


class Log:
    def __init__(self,action,detail,time):
        self.action = action
        self.detail = detail
        self.time = time
    
    def to_list(self):
        return [self.action,self.detail,self.time]
    
    def to_dict(self):
        return {
            "action" : self.action,
            "detail" : self.detail,
            "time" : self.time
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
        
        temp = []
        for n in data["note"]:
            note = Note(n["title"],n["content"])
            temp.append(note)
        data["note"] = temp
        
        temp = []
        for l in data["log"]:
            log = Log(l["action"],l["detail"],l["time"])
            temp.append(log)
        data["log"] = temp
        

except (FileNotFoundError, json.JSONDecodeError):
    data = {
        "task":[],
        "habit":[],
        "note":[],
        "log":[]
    }


f = Figlet(font = "standard")


def main():
    tasks = data["task"]
    habits = data["habit"]
    notes = data["note"]
    logs = data["log"]
    while True:
        clear()
        print("Menu\n1. Tasks\n2. Habits\n3. Notes\n4. Logs\n5. Stats\n6. Exit")
        main_menu_choice = input("Choice: ")
        match main_menu_choice:
            case "1":
                while True:
                    clear()
                    if not tasks:
                        print("No Tasks")
                    else:
                        print(tabulate([task.to_list() for task in tasks],headers =["Task","Priority","Completion"],tablefmt="fancy_grid"))
                    print()
                    print("Tasks Menu\n1. Add Task\n2. Mark Complete\n3. Mark Incomplete\n4. Remove Completed\n5. Exit")
                    task_menu_choice = input("Choice: ")
                    match task_menu_choice:
                        case "1":
                            add_task(input("Task: ").strip(),input("Priority: ").strip(),tasks)
                            add_log("Task Added",tasks[-1].task,logs)
                        case "2":
                            i = int_validation("Task Number: ",tasks)
                            if i is None:
                                continue
                            mark_task(i,tasks)
                            add_log("Task Completed",tasks[i-1].task,logs)
                        case "3":
                            i = int_validation("Task Number: ",tasks)
                            if i is None:
                                continue
                            unmark_task(i,tasks)
                            add_log("Task Uncompleted",tasks[i-1].task,logs)
                        case "4":
                            for task in tasks:
                                if task.done == "Complete":
                                    add_log("Task Removed",task.task,logs)
                            tasks[:] = [task for task in tasks if task.done != "Complete"]
                            
                        case "5":
                            break
                        case _:
                            invalid_input()
                    data["task"] = tasks

            case "2":
                while True:
                    clear()
                    if not habits:
                        print("No habits")
                    else:
                        print(tabulate([habit.to_list() for habit in habits],headers=["Habit","Frequency","Target"],tablefmt="fancy_grid"))
                    print()
                    print("Habits Menu\n1. Add Habit\n2. Remove Habit\n3. Exit")
                    habit_menu_choice = input("Choice: ")
                    match habit_menu_choice:
                        case "1":
                            add_habit(input("Habit: ").strip(),input("Frequency: ").strip(),input("Target: ").strip(),habits)
                            add_log("Habit Added",habits[-1].habit,logs)
                        case "2":
                            i = int_validation("Habit Number: ",habits)
                            if i is None:
                                continue
                            add_log("Habit Removed",habits[i-1].habit,logs)
                            remove_habit(i,habits)
                        case "3":
                            break
                        case _:
                            invalid_input()
                    data["habit"] = habits

            case "3":
                while True:
                    clear()
                    if not notes:
                        print("No Notes")
                    else:
                        print(tabulate([note.to_list() for note in notes],headers =["Title","Content"],tablefmt="fancy_grid"))
                    print()
                    print("Notes Menu\n1. Add Note\n2. Remove Note\n3. Exit")
                    note_menu_choice = input("Choice: ")
                    match note_menu_choice:
                        case "1":
                            add_note(input("Title: ").strip(),input("Content: ").strip(),notes)
                            add_log("Note Added",f"{notes[-1].title} - {notes[-1].content}",logs)
                        case "2":
                            i = int_validation("Note Number: ",notes)
                            if i is None:
                                continue
                            add_log("Note Removed",f"{notes[i-1].title} - {notes[i-1].content}",logs)
                            remove_note(i,notes)
                            
                        case "3":
                            break
                        case _:
                            invalid_input()
                    data["note"] = notes

            case "4":
                while True:
                    clear()
                    if not logs:
                        print("No Logs")
                    else:
                        print(tabulate([log.to_list() for log in logs],headers =["Action","Detail","Time"],tablefmt="fancy_grid"))
                    print()
                    print("Logs Menu\n1. Clear\n2. Exit")
                    log_menu_choice = input("Choice: ")
                    match log_menu_choice:
                        case "1":
                            logs.clear()
                        case "2":
                            break
                        case _:
                            invalid_input()
                    data["log"] = logs

            case "5":
                while True:
                    clear()
                    total_tasks = len(tasks)
                    completed_tasks = len([task for task in tasks if task.done == "Complete"])
                    total_habits = len(habits)
                    total_notes = len(notes)
                    total_logs = len(logs)
                    print("Stats")
                    print(f"Total Tasks: {total_tasks}")
                    print(f"Completed Tasks: {completed_tasks}")
                    print(f"Incomplete Tasks: {total_tasks - completed_tasks}")
                    print(f"Total Habits: {total_habits}")
                    print(f"Total Notes: {total_notes}")
                    print(f"Total Logs: {total_logs}")
                    print()
                    print("Stats Menu\n1. Exit")
                    stat_menu_choice = input("Choice: ")
                    match stat_menu_choice:
                        case "1":
                            break
                        case _:
                            invalid_input()
                            

            case "6":
                break

            case _:
                invalid_input()
                pass

    data["task"] = [task.to_dict() for task in tasks]
    data["habit"] = [habit.to_dict() for habit in habits]
    data["note"] = [note.to_dict() for note in notes]
    data["log"] = [log.to_dict() for log in logs]
    with open("data.json", "w") as file:
        json.dump(data,file,indent=4)


def add_task(task,priority,tasks):
    tasks.append(Task(task,priority))

def mark_task(i,tasks):
    tasks[i-1].done = "Complete"

def unmark_task(i,tasks):
    tasks[i-1].done = "Incomplete"

def add_habit(habit,frequency,target,habits):
    habits.append(Habit(habit,frequency,target))

def remove_habit(i,habits):
    del habits[i-1]

def add_note(title,content,notes):
    notes.append(Note(title,content))

def remove_note(i,notes):
    del notes[i-1]

def add_log(action,detail,logs):
    logs.append(Log(action,detail,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    if len(logs) > 100:
        del logs[0]

def int_validation(prompt,items):
    try:
        n = int(input(prompt))
        if n < 1 or n > len(items):
            raise ValueError
        return n
    except ValueError:
        invalid_input()
        return None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f.renderText("Productivity System"))

def invalid_input():
    print("\nInvalid Input!")
    time.sleep(0.75)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        data["task"] = [task.to_dict() for task in  data["task"]]
        data["habit"] = [habit.to_dict() for habit in data["habit"]]
        data["note"] = [note.to_dict() for note in data["note"]]
        data["log"] = [log.to_dict() for log in data["log"]]
        with open("data.json", "w") as file:
            json.dump(data,file,indent=4)
