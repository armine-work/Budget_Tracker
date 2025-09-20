import os
import logging
logging.basicConfig( level=logging.DEBUG,
                    filename = 'logs.txt',
                    format = '%(levelname)s - %(message)s - %(filename)s - %(asctime)s ',
                    datefmt = ' %H:%M:%S %m-%d-%Y',
                    filemode = 'w' )


#from app.validation_check import validate_number, get_full_name

from app.customer_data_input import *

from app.file_usage import *


from PersonBudget import PersonBudget, OnlineBudget


def main():
    ############################################### get customer's name, surname from user's input
    while True:
        select_input = input("How to input customer data? ['manually', 'text', 'json'] ").lower().strip()
        logging.debug(f"data selection input: [{select_input}]")
        if select_input in ['manually', 'text', 'json']:
            break
        else:
            print("Please enter one of these: 'manually', 'text', 'json'.")
            logging.error(f"wrong input from user[{select_input}]")

    if select_input == "manually":
        name = call_name()
        surname = call_surname()
        expense = call_expense(user_input="What is customer's first expense? ")
        balance = call_balance()
        loan_balance = call_loan_balance()
        while True:
            user_input = input("Would you like to get Online Loan? 'yes/no': ").strip().lower()
            if user_input == "yes".strip():
                online_loan = call_online_loan()
                ############################################################################# create customer instant using data with online loan
                online_customer = OnlineBudget(name, surname, balance, loan_balance, online_loan)
                ##################################################### calculate balance and get all transactions
                online_customer.balance_calculator(expense)
                transactions = online_customer.transactions_data
                online_customer.print_transactions()
                ################################################### write transactions to the Text and Json files
                write_data_to_text_file(transactions)
                write_data_to_json(transactions)
                break

            elif user_input == "no".strip():
                ############################################################################# create customer instant using data without online loan
                customer = PersonBudget(name, surname, balance, loan_balance)
                ##################################################### calculate balance and get all transactions
                customer.balance_calculator(expense)
                transactions = customer.transactions_data
                customer.print_transactions()
                ################################################### write transactions to the Text and Json files
                write_data_to_text_file(transactions)
                write_data_to_json(transactions)
                break
            else:
                print("Please enter one of these: 'yes/no'.")


    #############################################################################################################################
    elif select_input == "text":
        while True:
            # file_path = r"C:\projects\Budget_Tracker\CustomerData.txt"  ##### for testing use
            path_input = input("Enter file's path: ").strip()
            logging.debug(f"manually entered path: [{path_input}]")
            ############################################################### validate the inputted file's path
            file_name = "CustomerData.txt"
            if os.path.basename(path_input) == file_name:
                file_path = path_input
            else:
                file_path = os.path.join(path_input, file_name)
            ############################################################## get data from the file
            file_data = get_data_from_file(file_path)
            if file_data:
                name, surname, balance, loan_balance, expense = file_data
                break
            else:
                exit()
        ############################################################################# create customer instant using data from Text file
        customer = PersonBudget(name, surname, balance, loan_balance)
        ##################################################### calculate balance and get all transactions
        customer.balance_calculator(expense)
        transactions = customer.transactions_data
        ############################################################### print results
        customer.print_transactions()
        ################################################### write transactions to the Text and Json files
        write_data_to_text_file(transactions)
        write_data_to_json(transactions)


    elif select_input == "json":
        while True:
            path_input = input("Enter file's path: ").strip()
            file_name = "CustomerData.json"
            if os.path.basename(path_input) == file_name:
                file_path = path_input
            else:
                file_path = os.path.join(path_input, file_name)
            file_data = get_data_from_json(file_path)
            if file_data:
                name, surname, balance, loan_balance, expense = file_data
                break
            else:
                exit()
        ############################################################################# create customer instant using data from Json file
        customer = PersonBudget(name, surname, balance, loan_balance)
        ##################################################### calculate balance and get all transactions
        customer.balance_calculator(expense)
        transactions = customer.transactions_data
        ############################################################### print results
        customer.print_transactions()
        ################################################### write transactions to the Text and Json files
        write_data_to_text_file(transactions)
        write_data_to_json(transactions)


if __name__ == "__main__":
    main()
