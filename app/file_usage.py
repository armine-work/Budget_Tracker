from app.validation_check import get_number, get_full_name
from app.expense_input import get_expense

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
                balance = get_number(user_input="Enter user's current balance manually: ",
                                     error_ms="Please enter numeric, positive value for balance: ")
            ################### receive loan balance from the provided file, if data is incorrect, ask to provide it manually
            loan_file = file_data.readline().strip()
            if loan_file.replace(".", "", 1).isnumeric():
                loan_balance = float(loan_file) if '.' in loan_file else int(loan_file)
                print("The current Loan Balance from the provided file is:", loan_balance)
            else:
                print("The Loan Balance is invalid or missing in the provided file.")
                loan_balance = get_number(user_input="Enter user's loan balance manually: ",
                                          error_ms="Please enter numeric, positive value for loan balance: ")
                ################# ask user to input their first expense
            expense = get_expense("Enter user's first expense manually: ")
            return name, surname, balance, loan_balance, expense
    except FileNotFoundError as error:
        print(f"Provided file doesn't exist", {error})
        return None
    except Exception as error:
        print(f"An error occurred:", {error})
        return None
    ##################################################################### write transaction data into separate file


def write_data_to_file(expenses_sheet, balances_list, full_name ):
    with open("Transaction.txt", "w") as transaction_file:
        for i in range(len(expenses_sheet)):
            expense_in_file = expenses_sheet[i]["expense_count"]
            balance_in_file = balances_list[i][0]
            loan_in_file = balances_list[i][1]
            expense_ID_in_file = expenses_sheet[i]['expense_id']
            transaction_file.write(f"Full name: {full_name}, "
                                   f"Expense: {expense_in_file}, Balance: {balance_in_file}, Loan balance: {loan_in_file}, "
                                   f"Expense ID: {expense_ID_in_file}.\n")

    print("The transaction data is written to 'Transactions.txt'.")

