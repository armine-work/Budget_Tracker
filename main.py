#import os
import logging
logging.basicConfig( level=logging.DEBUG,
                    filename = 'logs.txt',
                    format = '%(levelname)s - %(message)s - %(filename)s - %(asctime)s ',
                    datefmt = ' %H:%M:%S %m-%d-%Y',
                    filemode = 'w' )
from app.validation_check import get_number, get_full_name
from app.expense_input import get_expense

from PersonBudget import PersonBudget, OnlineBudget


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

    expense = get_expense(user_input="What is customer's first expense? ")
    customer.balance_calculator(expense)
    customer.print_transactions()

    print("\n----------------Next customer ----------------\n")
    ######################################################################### get customers' online loan balance
    name = input("Enter new customer's name: ")
    logging.debug(f"new customer's name: {name}")
    #############
    surname = input("Enter new customer's surname: ")
    logging.debug(f"new customer's surname: {surname}")
    #############
    ############################################## get customer's balance & loan balance from user's input
    balance = get_number(user_input="What is new customer's current balance? ",
                          error_ms ="Please enter numeric, positive value for balance: ")
    logging.debug(f" new customer's current balance: [{balance}]")
    #############
    loan_balance = get_number(user_input="What is new customer's loan balance? ",
                              error_ms = "Please enter numeric, positive value for loan balance: ")
    logging.debug(f"new customer's loan balance: [{loan_balance}]")
    #############
    online_loan = get_number(user_input="What is new customer's online loan? ",
                             error_ms="Please enter numeric, positive value for online loan: ")
    logging.debug(f"customer's online loan: [{online_loan}]")
    #############

    online_customer = OnlineBudget(name, surname, balance, loan_balance, online_loan)
    
    expense = get_expense(user_input="What is customer's first expense? ")
    online_customer.balance_calculator(expense)
    online_customer.print_transactions()

if __name__ == "__main__":
    main()
