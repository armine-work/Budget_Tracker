#import os
import logging
logging.basicConfig(level=logging.DEBUG,

                    filename = 'logs.txt',
                    format = '%(levelname)s - %(message)s - %(filename)s - %(asctime)s ',
                    datefmt = ' %H:%M:%S %m-%d-%Y',
                    filemode = 'w' )
from app.validation_check import get_number, get_full_name
from app.expense_input import get_expense
from PersonBudget import PersonBudget

def main():
############################################### get customer's name, surname from user's input
    name = input("Enter customer's name: ")
    logging.debug(f"customer's name: {name}")
    #############
    surname = input("Enter customer's surname: ")
    logging.debug(f"customer's surname: {surname}")
    #############

    ############################################## get customer's balance & loan balance from user's input
    balance = get_number(user_input="What is customer's current balance? ",
                          error_ms ="Please enter numeric, positive value for balance: ")
    logging.debug(f"customer's current balance: [{balance}]")
    #############
    loan_balance = get_number(user_input="What is customer's loan balance? ",
                              error_ms = "Please enter numeric, positive value for loan balance: ")
    logging.debug(f"customer's loan balance: [{loan_balance}]")
    #############
############################################################################ get customer's full name
    customer = PersonBudget(name, surname, balance, loan_balance)

    full_name = get_full_name(name, surname)
    logging.debug(f"customer's full_name: [{full_name}]")
    #############
    expense = get_expense(user_input="What is customer's first expense? ")
    logging.debug(f"customer's first expense: [{expense}]")
    #############
    customer.balance_calculator(expense, full_name)
    customer.print_transactions(full_name)

if __name__ == "__main__":
    main()