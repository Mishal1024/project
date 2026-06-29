# Kyzen
   #### Video Demo: https://youtu.be/DVWaTDNpQ8k
   #### Description:
Kyzen is a Command Line productivity application build using python. It helps users organize and manage their tasks, habits and notes along with insights into their activity or progress, all within a terminal.

The main goal if the project is to create a lightweight personal productivity system that combines multiples tools to help users improve their life.

When the program starts it loads all the saved data from a JSON file named data.json. This allows the users to continue from where they left off. If no data file exists or if it fails to load it, the programs creates a dictionary with empty lists for keeping track of entries.

This application is menu driven and divided into fice sections:

1. Tasks: allows user to add tasks, assign priorities, mark taks as complete or incomplete and remove completed tasks.

2. Habits: Allow users to create habits with a frequency and target, and remove them.

3. Notes: Allow users to create notes with titles directly inside the program for important information without leaving the terminal as well as removing unwanted once.

4. Logs: Shows the activity history of the user limited to a 100 entries.

5. Stats: Shows a summary of the users productivity such as total tasks, completed tasks, incomplete tasks, notes and logs.

The project uses Object Oriented Programming with four classes namely Task, Habit, Note and Log. Each class stores its own data and provides methods for converting objects into lists for table display and into dictionaries for storing in JSON file.


Files

project.py
This is the main project file. It contains all classes, main logic and functions

test_project.py
This file contains unit tests written to verify that all the functions in the main project file is working properly.

data.json
This file acts as a database for the program to store all program data persistently.

requirements.txt
This file contains all the installable libraries that the project requires, one per line, it allows users to install them with the command "pip install -r requirements.txt". It includes pyfiglet for banner and tabulate for table formatting.


Design Choices

One of the main design choices in this project was structuring the program using four classes instead of dictionaries.

Another decision was to use JSON for storage instead of plan text. This allowed structured storage and made it easy to expand the project further.

I used tabulate for better appearance and user experience along with pyfiglet. While these are not necessarily functional, they improve usability.

I didn’t like how the terminal output kept getting longer as the program was used, so I implemented a clear() function that clears the screen and reprints the banner. This makes it feel like the application’s state is updating rather than simply appending another response.

I also decided to implement automatic logging system that automatically creates a log and stores it whenever an action that are worth recording takes place. This adds accountability and allows users to review their recent ectivity. To keep storage manageable I limited logs to the most recent 100 entries

In the future, I would like to add deadlines, habit streak tracking, search functionality, and notifications to make the system even more powerful.

This is my final project for CS50P. It brings together the core concepts I learned throughout the course and applied them in a practical way. Building this project helped me improve my understanding of Python and gave me experience designing a program from scratch