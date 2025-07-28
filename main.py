# With string operation, make better formatting for customer name, like removing extra spaces, and make capitalized name parts
# For each transaction, create a transaction ID in this format name.surname-id and store them in the data structure for transactions

# Add a new input value that will check if the name, balance and loan will be provided manually or from a file
# • If Yes, the program should work as before (in terms of input)
# • If No, the program should read data from a file called “CustomerData”. File path must be an additional input.
# Input file one line: Name, Surname, balance, loan
# • Write transactions in to a file called “Transaction.txt”

################################################################### store expenses and balances empty lists
expenses_sheet = []
balances_list = []
#################################################################### get loan balance
def get_loan_balance():
#################################################################### get valid number from user
def get_number(user_input, error_ms):
    while True:
        loan_balance_input = input("What is your active loan balance? ")
        if loan_balance_input.replace('.', '', 1).isnumeric():
            loan_balance = float(loan_balance_input) if '.' in loan_balance_input else int(loan_balance_input)
            return loan_balance
        else:
            print("Error!!! enter numeric value for the 'Loan Balance'.")

####################################################################### get balance
def get_balance():
    while True:
        balance_input = input("What is your balance? ")
        if balance_input.replace('.', '', 1).isnumeric():
            balance = float(balance_input) if '.' in balance_input else int(balance_input)
            return balance
        else:
            print("Error!!! enter numeric value for the 'Balance'.")

###################################################################### get first expense
def get_expense():
    while True:
        expense_input = input("What is your expense? ")
        if expense_input.replace('.', '', 1).isnumeric():
            expense = float(expense_input) if '.' in expense_input else int(expense_input)
            return expense
        else:
            print("Error!!! enter numeric value for the 'Expense'.")

######################################################################## call user's balances
loan_balance = get_loan_balance()
balance = get_balance()
expense = get_expense()
#################################################################### ask for data input choice
while True:
    select_input = input("Input data manually? yes/no: ").lower().strip()
    if select_input == "yes":
        ################################################################### receive name, surname from user
        name = input("What is user's name? ").strip()
        surname = input("What is user's surname? ").strip()
        ################################################## receive loan balance, current balance and first expense from user:
        loan_balance = get_number(user_input="What is user's loan balance? ",
                                  error_ms = "Please enter numeric, positive value for loan balance: ")
        balance = get_number(user_input="What is user's current balance? ",
                             error_ms ="Please enter numeric, positive value for balance: ")
        expense = get_number(user_input="What is user's first expense? ",
                             error_ms="Please enter numeric, positive value for expense: ")
        break
    elif select_input == "no":
        try:
            select_path = input("Enter file' path: ").strip()
            #select_path = r"C:\projects\Budget_Tracker\CustomerData.txt" ##### for testing use
            with open(select_path, "r") as file_data:
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
################## ask user to input their first expense
                expense = get_number(user_input="Enter user's first expense manually: ",
                                     error_ms="Please enter numeric, positive value for expense: ")
                break
        except FileNotFoundError as error:
            print(f"Provided file {select_path} doesn't exist", {error})
        except Exception as error:
            print(f"An error occurred:", {error})
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
################################################################### remove extra spaces
full_name = name.title() + " " + surname.title()
full_name_split = full_name.split()
full_name = " ".join(full_name_split)
# print("full name is", full_name)

expense_count = 0
done = False

while not done:
    expense_count += 1
    if expense <= balance:
        balance = balance - expense
        print("___ATTENTION___ Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, the loan is {loan_balance}:")
    elif expense <= balance + loan_balance:
        print("___WARNING___ You don't have enough balance, the purchase will be done from your active loan balance.")
        debt = balance - expense
        loan_balance -= abs(debt)
        balance = 0
        print("___ATTENTION___ Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, and the loan is: {loan_balance}")
    else:
        print(f"___WARNING___ Your expense [{expense}] is more than your funds: [loan:{loan_balance} + balance:{balance}].")
        print("The purchase couldn't be done.")
        break
    ##################################################################### create expenses ID after each transaction
    space_count = full_name.count(" ")
    username = full_name.replace(" ", ".")
    expense_id = username.lower() + "-" + str(expense_count)
    #print(f"{full_name} customer's expense ID is {expense_id}.")

    #####################################################################armi store expenses in dictionary
    expenses_data = {"expense_count": expense,
                     "expense_id": expense_id}
    ##################################################################### convert expenses data to a list
    expenses_sheet.append(expenses_data)
    ##################################################################### store balance with loan balance in a tuple
    balances_tuple = tuple((balance, loan_balance))
    ##################################################################### convert balance data to a list, so it can be added more
    balances_list.append(balances_tuple)
    ##################################################################### ask for a new expense
    while True:
        next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower().strip()
        if next_expense_prompt == "yes":
            while True:
                new_expense_input = input("What is your new expense? ")
                if new_expense_input.replace('.', '', 1).isnumeric():
                    expense = float(new_expense_input) if '.' in new_expense_input else int(new_expense_input)
                    break
                else:
                    print("Please, enter numeric value for the 'New Expense'.")
            break
        elif next_expense_prompt == "no":
            print("Ok, thank you. The purchase process is finished.")
            done = True
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

############################################################################ print the results
print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
if len(expenses_sheet) == 0:
    print("No purchase has been done. Thank you for using Budget Tracker.")
else:
    for i in range(len(expenses_sheet)):
        print(f"{i+1}) Expense: {expenses_sheet[i]["expense_count"]},"
              f" Balance: {balances_list[i][0]}, Loan: {balances_list[i][1]}."
              f"\n  Expense ID is: {expenses_sheet[i]['expense_id']}.")
############################################################################# write data into separate file
    with open("Transaction.txt", "w") as transaction_file:
        for i in range(len(expenses_sheet)):
            expense_in_file = expenses_sheet[i]["expense_count"]
            balance_in_file = balances_list[i][0]
            loan_in_file = balances_list[i][1]
            expense_ID_in_file = expenses_sheet[i]['expense_id']
            transaction_file.write(f"Full name: {full_name}, "
                                   f"Expense: {expense_in_file}, Balance: {balance_in_file}, Loan balance: {loan_in_file}, "
                                   f"Expense ID: {expense_ID_in_file}.\n")

    print("\nAll transaction data is written to 'Transactions.txt'.")
