Simple Script to Save and Analyze Expenses
This script allows you to manage your expenses directly from the command line. Below are the available commands and their functionalities.

Command Line Usage

1. Add Expense
Command: add <amount> <description>
Description: Adds a new expense to the list.
Example:

add 150.75 "Groceries"

2. Generate Report
Command: report
Description: Generates a report of all recorded expenses with their descriptions.
Example:

report

3. Remove Expense
Command: remove <expense ID>
Description: Removes an expense from the list by its ID.
Example:

remove 2

4. Import Expenses from CSV
Command: importcsv <csv file>
Description: Imports expenses from a specified CSV file and appends them to the existing list.
Example:

importcsv expenses.csv

5. Export Expenses in Python Format
Command: exportpython
Description: Prints all entries in a Python-recognizable format.
Example:

exportpython

Script Details
Expense Class
A data class representing an expense, containing:

id (int): Unique identifier for the expense.
amount (float): The amount spent.
description (str): Description of the expense.
Functions
gen_id(stored_expenses: List[Expense]) -> int
Generates a unique ID for each expense.

read_expense_list(file: str) -> List[Expense]
Reads the list of expenses from the file.

file_save(expenses: List[Expense], file: str) -> None
Saves the list of expenses to the file.

from_csv(file: str, expenses: List[Expense]) -> List[Expense]
Imports expenses from a CSV file.

print_report(expenses: List[Expense]) -> None
Prints a report of all expenses.

Click Commands
add(arg1, arg2)
Adds a new expense.

remove(id)
Removes an expense by its ID.

report()
Generates and prints a report of all expenses.

importcsv(csv_file)
Imports expenses from a CSV file.

exportpython()
Exports all expenses in a Python-recognizable format.

Example CSV File Format
The CSV file should have the following format:

amount,description
100.50,"Electricity bill"
200.75,"New shoes"
