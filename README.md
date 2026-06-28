# CLI Productivity System
   #### Video Demo:
   #### Description:
This is a Command Line productivity application build using python. It helps users organize and manage their tasks, habits and notes along with insights into their activity or progress, all within a terminal.

The main goal if the project is to create a lightweight personal productivity system that combines multiples tools to help users improve their life.

When the program starts it loads all the saved data from a JSON file named data.json. This allows the users to continue from where they left off. If no data file exists or if it fails to load it, the programs creates a dictionary with empty lists for keeping track of entries.

This application is menu driven and divided into fice sections:

1. Tasks: allows user to add tasks, assign priorities, mark taks as complete or incomplete and remove completed tasks.

2. Habits: Allow users to create habits with a frequency and target, and remove them.

3. Notes: Allow users to create notes with titles directly inside the program for important information without leaving the terminal as well as removing unwanted once.

4. Logs: Shows the activity history of the user limited to a 100 entries.

5. Stats: Shows a summary of the users productivity such as total tasks, completed tasks, incomplete tasks, notes and logs.

The project uses Object Oriented Programming with four classes namely Task, Habit, Note and Log. Each class stores its own data and provides methods for converting objects into lists for table display and into dictionaries for storing in JSON file.

####Files
