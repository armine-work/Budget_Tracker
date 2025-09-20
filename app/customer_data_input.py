import logging
logger = logging.getLogger(__name__)

from app.validation_check import validate_number

def call_name ():
    name = input("Enter customer's name: ")
    logging.debug(f"new customer's name: {name}")
    #############
    return name


def call_surname ():
    surname = input("Enter customer's surname: ")
    logging.debug(f"new customer's surname: {surname}")
    #############
    return surname


def call_balance ():
        ############################################## get customer's balance & loan balance from user's input
    balance = validate_number(user_input="What is customer's current balance? ",
                              error_ms ="Please enter numeric, positive value for balance: ")
    logging.debug(f" new customer's current balance: [{balance}]")
    #############
    return balance

def call_loan_balance ():
    loan_balance = validate_number(user_input="What is customer's loan balance? ",
                                   error_ms = "Please enter numeric, positive value for loan balance: ")
    logging.debug(f"new customer's loan balance: [{loan_balance}]")
    #############
    return loan_balance


def call_online_loan ():
    online_loan = validate_number(user_input="What is customer's online loan? ",
                                  error_ms="Please enter numeric, positive value for online loan: ")
    logging.debug(f"customer's online loan: [{online_loan}]")
    #############
    return online_loan



############################################################################# get expense from user
def call_expense(user_input):
    expense = validate_number(user_input, error_ms="Please enter numeric, positive value for expense: ")
    return expense