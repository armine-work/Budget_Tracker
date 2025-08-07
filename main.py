# Add a new input value that will check if the name, balance and loan will be provided manually or from a file
# • If Yes, the program should work as before (in terms of input)
# • If No, the program should read data from a file called “CustomerData”. File path must be an additional input.
# Input file one line: Name, Surname, balance, loan
# • Write transactions in to a file called “Transaction.txt”
import os
from app.validation_check import get_number, get_full_name
from app.file_usage import write_data_to_file, get_data_from_file
from app.expense_input import get_expense
from app.balances import balance_calculator

################################################################### store expenses and balances in empty lists
expenses_sheet = []
balances_list = []

#################################################################### ask for data input choice
while True:
    select_input = input("Do you want to enter data manually? yes/no: ").lower().strip()
    if select_input in ["yes", "no"]:
        break
    else:
        print("Please enter yes or no.")

if select_input == "yes":
    ################################################################### receive name, surname from user
    name = input("What is user's name? ").strip()
    surname = input("What is user's surname? ").strip()
    ################################################## receive loan balance, current balance and first expense from user:
    loan_balance = get_number(user_input="What is user's loan balance? ",
                              error_ms = "Please enter numeric, positive value for loan balance: ")
    balance = get_number(user_input="What is user's current balance? ",
                         error_ms ="Please enter numeric, positive value for current balance: ")

    ################################################################# call expense function
    expense = get_expense("What is user's first expense? ")
    print("first expense: ", expense)

else:
    while True:
        # file_path = r"C:\projects\Budget_Tracker\CustomerData.txt"  ##### for testing use
        path_input = input("Enter file's path: ").strip()
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

############################################################################ call the expanses calculator
full_name = get_full_name(name, surname)
balance_calculator(expense, balance, loan_balance, full_name, expenses_sheet, balances_list)

############################################################################ print the results
print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
if len(expenses_sheet) == 0:
    print("No purchase has been done. Thank you for using Budget Tracker.")
else:
    for i in range(len(expenses_sheet)):
        print(f"{i+1}) Expense: {expenses_sheet[i]["expense_count"]},"
              f" Balance: {balances_list[i][0]}, Loan: {balances_list[i][1]}."
              f"\n  Expense ID is: {expenses_sheet[i]['expense_id']}.")


