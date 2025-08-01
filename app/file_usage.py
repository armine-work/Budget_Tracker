from app import validation_check


############################################################################## store data from user in function file_path
def get_data_from_file(file_path):
    try:
        with open(file_path, "r") as file_data:
            ################################################################### read user's name and surname form the provided file
            name = file_data.readline().strip()
            if len(name) == 0:
                name = input("Name is missing in the provided file. \n Enter user's name manually: ")
            surname = file_data.readline().strip()
            if len(surname) == 0:
                surname = input("Surname is missing in the provided file. \n Enter user's surname manually: ")
            ################### receive current balance from the provided file, if data is incorrect, ask to provide it manually
            balance_file = file_data.readline().strip()
            if balance_file.replace(".", "", 1).isnumeric():
                balance = float(balance_file) if '.' in balance_file else int(balance_file)
                print("The Current Balance from the provided file is:", balance)
            else:
                print("The Balance is invalid or missing in the provided file.")
                balance = validation_check.get_number(user_input="Enter user's current balance manually: ",
                                     error_ms="Please enter numeric, positive value for balance: ")
            ################### receive loan balance from the provided file, if data is incorrect, ask to provide it manually
            loan_file = file_data.readline().strip()
            if loan_file.replace(".", "", 1).isnumeric():
                loan_balance = float(loan_file) if '.' in loan_file else int(loan_file)
                print("The current Loan Balance from the provided file is:", loan_balance)
            else:
                print("The Loan Balance is invalid or missing in the provided file.")
                loan_balance = validation_check.get_number(user_input="Enter user's loan balance manually: ",
                                          error_ms="Please enter numeric, positive value for loan balance: ")
                ################# ask user to input their first expense
            expense = validation_check.get_number(user_input="Enter user's first expense manually: ",
                                     error_ms="Please enter numeric, positive value for expense: ")
            return name, surname, balance, loan_balance, expense
    except FileNotFoundError as error:
        print(f"Provided file doesn't exist", {error})
        return None
    except Exception as error:
        print(f"An error occurred:", {error})
        return None


