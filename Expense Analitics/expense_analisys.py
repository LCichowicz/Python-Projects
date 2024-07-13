import csv
from dataclasses import dataclass
from pickle import load, dump
from typing import List
import sys

import click

FILE = 'budget.db'
EXPENSE_TRESCHOLD = 500   

@dataclass
class Expense:
    id:int
    amount:float
    description: str

    def __post__init__(self):
        if not self.description:
            raise ValueError('Description cannot be empty')
        if self.amount < 0:
            raise ValueError('Amount has to be greater or equal to 0')
        
def gen_id(stored_expenses:List[Expense])->int:
    ids = {e.id for e in stored_expenses}
    counter = 1
    while True:
        if counter in ids:
            counter +=1
        else: 
            break
    return counter

def read_Expense_list(file:str)-> List[Expense]:
    try:
        with open(file, 'rb') as reader:
            expenses = load(reader)   
    except FileNotFoundError:
        expenses = []

    return expenses

def file_save(expenses:List[Expense], file)->None:
    with open(file, 'wb') as writter:
        dump(expenses, writter)
        print('Succes!!!')

def from_csv(file:str, expenses:List[Expense])->List[Expense]:
    
    all_expenses = []
    for item in expenses:
        all_expenses.append(item)

    with open(file, encoding='utf-8') as reader:
        imported_expenses = csv.DictReader(reader)
        for expense in imported_expenses:
            expense = Expense(id=gen_id(all_expenses),
                              amount=float(expense['amount']), 
                              description=expense['description'])
            all_expenses.append(expense)

    return all_expenses
    

def print_report(expenses:List[Expense])->None:
    if expenses:
        print(f'{'ID':<4}{'Amount':<7}{'BIG?':^5}{'Descripton':>20}')
        expenses = sorted(expenses, key= lambda x: x.id)
        for e in expenses:
            if e.amount>EXPENSE_TRESCHOLD:
                big = 'YES'
            else:
                big = ''
            print(f'{e.id:<4}{e.amount:<7}{big:^5}{e.description:>20} ')

        total = sum([e.amount for e in expenses])

        print(f'Total expenses: {total} zł')
    else:
        print(f'There are no entries in {FILE} file or it does not exists!!!')


@click.group()
def cli():
    pass


@cli.command()
@click.argument('arg1')
@click.argument('arg2')
def add(arg1, arg2):
    try: 
        amount = float(arg1)
        new_expense = arg2
    except ValueError:
        try:
            amount = float(arg2)
            new_expense = arg1
        except ValueError:
            print('At least one argument have to be a valid numer representing amount')
            sys.exit()
    
    expenses = read_Expense_list(FILE)

    try:
        expense = Expense(id=gen_id(expenses), amount=amount, description=new_expense)
    except ValueError as e:
        print(f'Error occurred.{e.args[0]}')

    expenses.append(expense)
    file_save(expenses, FILE)


@cli.command()
@click.argument('id')
def remove(id):
    try:
        id = int(id)
    except ValueError:
        print('To remove an item You have to indicate correct expense ID')
        sys.exit()

    expenses = read_Expense_list(FILE)
    for expense in expenses:
        if expense.id == id:
            expenses.remove(expense)
            print('Item has been deleted')
            break

    print_report(expenses)
    file_save(expenses, FILE)


    
@cli.command()
def report():

    expenses = read_Expense_list(FILE) 
    print_report(expenses)


@cli.command()
@click.argument('csv_file')
def importcsv(csv_file):

    expenses = read_Expense_list(FILE)
    expenses_old_and_new = from_csv(csv_file,expenses)
    print_report(expenses_old_and_new)
    file_save(expenses_old_and_new, FILE)


@cli.command()
def exportpython():
    expenses = read_Expense_list(FILE)
    for item in expenses:
        print(item)




if __name__ == '__main__':
    cli()