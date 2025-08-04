from app import validation_check
import logging
logger = logging.getLogger(__name__)

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
            surname = file_data.readline().strip()
            #############################################################
            logger.info(f"user's surname from file: [{surname}]")
            if len(surname) == 0:
                surname = input("Surname is missing in the provided file. \nEnter user's surname manually: ")
                logger.info(f"user's surname provided manually: [{surname}]")

            ################### receive current balance from the provided file, if data is incorrect, ask to provide it manually
            balance_file = file_data.readline().strip()
            if balance_file.replace(".", "", 1).isnumeric():
                balance = float(balance_file) if '.' in balance_file else int(balance_file)
                print("The Current Balance from the provided file is:", balance)
                logger.info(f"user's balance from file: [{balance_file}]")
            else:
                print("The Balance is invalid or missing in the provided file.")
                balance = validation_check.get_number(user_input="Enter user's current balance manually: ",
                                     error_ms="Please enter numeric, positive value for balance: ")
                logger.info(f"user's balance provided manually: [{balance_file}]")

            ################### receive loan balance from the provided file, if data is incorrect, ask to provide it manually
            loan_file = file_data.readline().strip()
            if loan_file.replace(".", "", 1).isnumeric():
                loan_balance = float(loan_file) if '.' in loan_file else int(loan_file)
                print("The current Loan Balance from the provided file is:", loan_balance)
                logger.info(f"user's Loan-Balance from file: [{loan_balance}]")
            else:
                print("The Loan Balance is invalid or missing in the provided file.")
                loan_balance = validation_check.get_number(user_input="Enter user's loan balance manually: ",
                                          error_ms="Please enter numeric, positive value for loan balance: ")
                logger.info(f"user's Loan-Balance provided manually: [{loan_balance}]")

                ################# ask user to input their first expense
            expense = validation_check.get_number(user_input="Enter user's first expense manually: ",
                                     error_ms="Please enter numeric, positive value for expense: ")
            logger.info(f"user's first expense provided manually: [{expense}]")
            ##########################################################################
            return name, surname, balance, loan_balance, expense

    except FileNotFoundError as error:
        print(f"Provided file doesn't exist", {error})
        logger.exception(f"FileNotFoundError: [{error}]")
        return None
    except Exception as error:
        print(f"An error occurred:", {error})
        logger.exception(f"Exception: [{error}]")
        return None


