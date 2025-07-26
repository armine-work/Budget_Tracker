# Create a script that gets the full name, balance, expense, and active loan balance of a customer
# Calculate and print the balance after the expense.
# If the customer spends from the loan, then tell about it.
# Add one more input, which asks about a new expense. If yes, continue inputting; if no, stop inputting.
# Stop inputting if the customer spends the whole balance and the loan
# Change the code to save the balance and loan in lists after each expense
# Change the code to use a list for saving the expenses, Use the lists to print the necessary data
# Refactor code to use at least two types of data structures for working with data:
# For example: Expenses as a dictionary, Initial balances as tuples
# With string operation, make better formatting for customer name, like removing extra spaces, and make capitalized name parts
# For each transaction, create a transaction ID in this format name.surname-id and store them in the data structure for transactions

#################################################################### check user's input for name surname
def get_username(name_input):
    space_count = name_input.count(" ")
    if space_count !=0:
        name_input = name_input.replace(" ", "")
    if name_input.islower() == True:
        name_input = name_input.capitalize()
    if name_input.isupper() == True:
        name_input = name_input.lower().capitalize()

    return name_input

################################################################### call user full name
name = get_username(name_input=input("Whats your name? "))
surname = get_username(name_input=input("Whats your surname? "))
full_name = f"{name} {surname}"
###################################################################
expenses_sheet = []
balances_list = []
############################################### validate user's input
def get_number(user_input, error_ms):
    while True:
        user_input_number = input(user_input).strip()
        if user_input_number.replace(".", "", 1).isnumeric():
            user_input_number = float(user_input_number) if '.' in user_input_number else int(user_input_number)
            return user_input_number
        else:
            print(error_ms)

####################### receive loan balance, current balance and first expense from user:
loan_balance = get_number(user_input="What's your loan balance? ",
                          error_ms = "Please enter numeric, positive value for loan balance: ")

balance = get_number(user_input="What's your current balance? ",
                     error_ms ="Please enter numeric, positive value for balance: ")

expense = get_number(user_input="What's your expense? ",
                     error_ms="Please enter numeric, positive value for expense: ")



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
    expense_id = name.lower() + "." + surname.lower() + "-" + str(expense_count)
    # print(f"{full_name} customer's expense ID is {expense_id}.")
######################################################################### store expenses in dictionary
    expenses_data = {"expense_count": expense,
                     "expense_id": expense_id}
####################################################################### convert expenses data to a list, ???
    expenses_sheet.append(expenses_data)
##################################################################### store balance with loan balance in a tuple
    balances_tuple = tuple((balance, loan_balance))
##################################################################### convert balance data to a list, so it can be added more
    balances_list.append(balances_tuple)
##################################################################### ask for a new expense
    while True:
        next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower().strip()
        if next_expense_prompt == "yes":
            expense = get_number(user_input="What's your new expense? ",
                                 error_ms="Please enter numeric, positive value for expense: ")
            break
        elif next_expense_prompt == "no":
            print("Ok, thank you. The purchase process is finished.")
            done = True
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'. ")

################################################################################################
print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
if len(expenses_sheet) == 0:
    print("No purchase has been done. Thank you for using Budget Tracker.")
else:
    for i in range(len(expenses_sheet)):
        print(f"{i+1}) Expense: {expenses_sheet[i]["expense_count"]},"
              f" Balance: {balances_list[i][0]}, Loan: {balances_list[i][1]}."
              f"\n  Expense ID is: {expenses_sheet[i]['expense_id']}.")
