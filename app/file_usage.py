import logging
logger = logging.getLogger(__name__)

import json

from app.validation_check import validate_number, get_full_name

from app.customer_data_input import call_expense


############################################################################## store data from user in function file_path
def get_data_from_file(file_path):
    try:
        with open(file_path, "r") as file_data:
            ################################################################### read user's name and surname form the provided file
            name = file_data.readline().strip()
            logger.info(f"user's name from file: [{name}]")
            if len(name) == 0:
                name = input("Name is missing in the provided file. \nEnter user's name manually: ")
                logger.info(f"user's name provided manually: [{name}]")
                ###########

            surname = file_data.readline().strip()
            logger.info(f"user's surname from file: [{surname}]")
            if len(surname) == 0:
                surname = input("Surname is missing in the provided file. \nEnter user's surname manually: ")
                logger.info(f"user's surname provided manually: [{surname}]")
                ###########

            ################### receive current balance from the provided file, if data is incorrect, ask to provide it manually
            balance_file = file_data.readline().strip()
            if balance_file.replace(".", "", 1).isnumeric():
                balance = float(balance_file) if '.' in balance_file else int(balance_file)
                print("The Current Balance from the provided text file is:", balance)
                logger.info(f"user's balance from file: [{balance_file}]")
                ###########
            else:
                print("The Balance is invalid or missing in the provided file.")
                balance = validate_number(user_input="Enter user's current balance manually: ",
                                          error_ms="Please enter numeric, positive value for balance: ")
                logger.info(f"user's balance provided manually: [{balance_file}]")
                ###########

            ################### receive loan balance from the provided file, if data is incorrect, ask to provide it manually
            loan_file = file_data.readline().strip()
            if loan_file.replace(".", "", 1).isnumeric():
                loan_balance = float(loan_file) if '.' in loan_file else int(loan_file)
                print("The current Loan Balance from the provided text file is:", loan_balance)
                logger.info(f"user's Loan-Balance from file: [{loan_balance}]")
                ###########
            else:
                print("The Loan Balance is invalid or missing in the provided file.")
                loan_balance = validate_number(user_input="Enter user's loan balance manually: ",
                                               error_ms="Please enter numeric, positive value for loan balance: ")
                logger.info(f"user's Loan-Balance provided manually: [{loan_balance}]")
                ###########
                ################# ask user to input their first expense
            ################### receive current balance from the provided file, if data is incorrect, ask to provide it manually
            expense_file = file_data.readline().strip()
            if expense_file.replace(".", "", 1).isnumeric():
                expense = float(expense_file) if '.' in expense_file else int(expense_file)
                print("The first expense from the provided text file is:", expense)
                logger.info(f"user's 1 expense from file: [{expense_file}]")
                ###########
            else:
                print("The expense is invalid or missing in the provided file.")
                expense = validate_number(user_input="Enter user's expense manually: ",
                                          error_ms="Please enter numeric, positive value for first expense: ")
                logger.info(f"user's first expense provided manually: [{expense_file}]")
                ###########
            #
            # expense = get_number(user_input="Enter user's first expense manually: ",
            #                      error_ms="Please enter numeric, positive value for expense: ")
            # logger.info(f"user's first expense provided manually: [{expense}]")
            ##########
            return name, surname, balance, loan_balance, expense

    except FileNotFoundError as error:
        print(f"Provided file doesn't exist", {error})
        logger.exception(f"FileNotFoundError: [{error}]")
        ###############
        return None
    except Exception as error:
        print(f"An error occurred:", {error})
        logger.exception(f"Exception: [{error}]")
        ###############
        return None

    ##################################################################### write transaction data into separate file


def write_data_to_text_file(transactions):
    with open("transactions.txt", "w") as t_file:
        for i, transaction in enumerate(transactions, start=1):
               t_file.write(f"{i}) Expense: {transaction['expense']}, "
                     f" Balance: {transaction['balance']}, "
                     f" Loan: {transaction['loan_balance']},"
                     f" Online Loan: {transaction['online_loan']}."
                     f" Expense ID is: {transaction['expense_id']}\n")


               logging.debug(f"Expense: {transaction['expense']}, "
                     f"Balance: {transaction['balance']}, Loan: {transaction['loan_balance']}, Online Loan: {transaction['online_loan']}, Expense ID: {transaction['expense_id']}")

    logger.info("The transaction data is written to 'transactions.txt'.")
    print("\nThe transaction data is written to 'transactions.txt'.")
    ############


################################################################### get data from json file
def get_data_from_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)

                # check required keys
            required_keys = ["name", "surname", "balance", "loan_balance", "expense"]
            for key in required_keys:
                if key not in data:
                    print(f"Error: JSON file missing key '{key}'")
                    return None
            print("Name from the provided JSON file is:", data["name"])
            print("Surname from the provided JSON file is:", data["surname"])
            print("Loan Balance from the provided JSON file is:", data["loan_balance"])
            print("Balance from the provided JSON file is:", data["balance"])

            print("First Expense from the provided JSON file is:", data["expense"])
            return (
                data["name"],
                data["surname"],
                data["balance"],
                data["loan_balance"],
                data["expense"]
            )

    except FileNotFoundError as error:
        print(f"Provided file doesn't exist", {error})
        logger.exception(f"FileNotFoundError: [{error}]")
        return None
    except json.JSONDecodeError as error:
        print("Error: Invalid JSON format in file.", {error})
        logger.exception(f"FileNotFoundError: [{error}]")
        return None
    except Exception as error:
        print(f"An error occurred:", {error})
        logger.exception(f"Exception: [{error}]")
        return None


def write_data_to_json(transactions):
    with open("Transactions.json", "w") as j_file:
            json.dump(transactions, j_file)

    logger.info("The transaction data is written to 'Transactions.json'.")
    print("The transaction data is written to 'Transactions.json'.")
