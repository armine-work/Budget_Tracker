# With string operation, make better formatting for customer name, like removing extra spaces, and make capitalized name parts
# For each transaction, create a transaction ID in this format name.surname-id and store them in the data structure for transactions

# Add a new input value that will check if the name, balance and loan will be provided manually or from a file
# • If Yes, the program should work as before (in terms of input)
# • If No, the program should read data from a file called “CustomerData”. File path must be an additional input.
# Input file one line: Name, Surname, balance, loan
# • Write transactions in to a file called “Transaction.txt”
import os
import logging
logging.basicConfig(
                    level=logging.DEBUG,
                    filename = 'logs.txt',
                    format = '%(levelname)s - %(message)s - %(filename)s - %(asctime)s ',
                    datefmt = ' %H:%M:%S %m-%d-%Y',
                    filemode = 'w' )
from app.validation_check import get_number
from app.file_usage import get_data_from_file

################################################################### store expenses and balances in empty lists
expenses_sheet = []
balances_list = []

#################################################################### ask for data input choice
while True:
    select_input = input("Do you want to enter data manually? yes/no: ").lower().strip()
    logging.debug(f"data selection input: [{select_input}]")
    if select_input in ["yes", "no"]:
        break
    else:
        print("Please enter yes or no.")
        logging.error(f"wrong input from user[{select_input}]")

if select_input == "yes":
    ################################################################### receive name, surname from user
    name = input("What is user's name? ").strip()
    logging.debug(f"user's name: [{name}]")
    surname = input("What is user's surname? ").strip()
    logging.debug(f"user's surname: [{surname}]")
    ################################################## receive loan balance, current balance and first expense from user:
    loan_balance = get_number(user_input="What is user's loan balance? ",
                              error_ms = "Please enter numeric, positive value for loan balance: ")
    logging.debug(f"user's loan balance: [{loan_balance}]")

    balance = get_number(user_input="What is user's current balance? ",
                         error_ms ="Please enter numeric, positive value for balance: ")
    logging.debug(f"user's current balance: [{balance}]")

    expense = get_number(user_input="What is user's first expense? ",
                         error_ms="Please enter numeric, positive value for expense: ")
    logging.debug(f"user's first expense: [{expense}]")
else:
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

################################################################### remove extra spaces and get full name
full_name = name.title() + " " + surname.title()
full_name_split = full_name.split()
full_name = " ".join(full_name_split)
logging.debug(f"full name after formatting: [{full_name}]")

expense_count = 0
done = False

while not done:
    expense_count += 1
    if expense <= balance:
        balance = balance - expense
        print("\n___ATTENTION___ Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, the loan is {loan_balance}:")
        logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, the loan is {loan_balance}:")
    elif expense <= balance + loan_balance:
        print("You don't have enough balance, the purchase will be done from your active loan balance.")
        debt = balance - expense
        loan_balance -= abs(debt)
        balance = 0
        print("\n___ATTENTION___ Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, and the loan is: {loan_balance}")
        logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, and the loan is: {loan_balance}")
    else:
        print(f"{full_name}'s expense [{expense}] is more than funds: [loan:{loan_balance} + balance:{balance}].")
        print("The purchase couldn't be done. \nClosing the program")
        logging.warning(f"{full_name}'s expense [{expense}] is more than funds: [loan:{loan_balance} + balance:{balance}].")
        break
    ##################################################################### create expenses ID after each transaction
    space_count = full_name.count(" ")
    username = full_name.replace(" ", ".")
    expense_id = username.lower() + "-" + str(expense_count)
    logging.debug(f"{full_name} customer's expense ID is {expense_id}.")

    #####################################################################armi store expenses in dictionary
    expenses_data = {"expense_count": expense,
                     "expense_id": expense_id}
    ##################################################################### convert expenses data to a list
    expenses_sheet.append(expenses_data)
    ##################################################################### store balance with loan balance in a tuple
    balances_tuple = tuple((balance, loan_balance))
    ##################################################################### convert balance data to a list, so it can be added more
    balances_list.append(balances_tuple)

    ##################################################################### write transaction data into separate file
    with open("Transaction.txt", "w") as transaction_file:
        for i in range(len(expenses_sheet)):
            expense_in_file = expenses_sheet[i]["expense_count"]
            balance_in_file = balances_list[i][0]
            loan_in_file = balances_list[i][1]
            expense_ID_in_file = expenses_sheet[i]['expense_id']
            transaction_file.write(f"Full name: {full_name}, "
                                   f"Expense: {expense_in_file}, Balance: {balance_in_file}, Loan balance: {loan_in_file},"
                                   f"Expense ID: {expense_ID_in_file}.\n")
    logging.info("The transaction data is written to 'Transactions.txt'.")

    ##################################################################### ask for a new expense
    while True:
        next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower().strip()
        logging.debug(f"next expense prompt: [{next_expense_prompt}]")
        if next_expense_prompt == "yes":
            expense = get_number(user_input="What's your new expense? ",
                                 error_ms="Please enter numeric, positive value for expense: ")
            logging.debug(f"new expense: [{expense}]")
            break
        elif next_expense_prompt == "no":
            print("Ok, thank you. The purchase process is finished.")
            logging.info("The purchase process is finished.")
            done = True
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            logging.error(f"wrong input from user [{next_expense_prompt}]")

############################################################################ print the results
print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
if len(expenses_sheet) == 0:
    print("No purchase has been done. Thank you for using Budget Tracker.")
    logging.info("No purchase has been done.")
else:
    for i in range(len(expenses_sheet)):
        print(
              f"{i+1}) Expense: {expenses_sheet[i]["expense_count"]},"
              f" Balance: {balances_list[i][0]}, Loan: {balances_list[i][1]}."
              f"\n  Expense ID is: {expenses_sheet[i]['expense_id']}.")
        logging.info(
              f"\n {i+1}) Expense: {expenses_sheet[i]["expense_count"]},"
              f" Balance: {balances_list[i][0]}, Loan: {balances_list[i][1]}."
              f"\n  Expense ID is: {expenses_sheet[i]['expense_id']}.")


