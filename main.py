# Create a script that gets the full name, balance, expense, and active loan balance of a customer
# Calculate and print the balance after the expense.
# If the customer spends from the loan, then tell about it.
# Add one more input, which asks about a new expense. If yes, continue inputting; if no, stop inputting.
# Stop inputting if the customer spends the whole balance and the loan
# Change the code to save the balance and loan in lists after each expense
# Change the code to use a list for saving the expenses
# Use the lists to print the necessary data
name = input("What is your name? ")
surname = input("What is your surname? ")
full_name = name + " " + surname
# print("The customer's full name is", full_name)

while True:
    loan_balance_input = input("What is your active loan balance? ")
    if loan_balance_input.replace('.', '', 1).isnumeric():
        if '.' in loan_balance_input:
            loan_balance = float(loan_balance_input)
        else:
            loan_balance = int(loan_balance_input)
    else:
        print("Please, enter numeric value for the 'Loan Balance'.")
        continue
    break

while True:
    balance_input = input("What is your balance? ")
    if balance_input.replace('.', '', 1).isnumeric():
        if '.' in balance_input:
            balance = float(balance_input)
        else:
            balance = int(balance_input)
    else:
        print("Please, enter numeric value for the 'Balance'.")
        continue
    break

while True:
    expense_input = input("What is your expense? ")
    if expense_input.replace('.', '', 1).isnumeric():
        if '.' in expense_input:
            expense = float(expense_input)
        else:
            expense = int(expense_input)
    else:
        print("Please, enter numeric value for the 'Expense'.")
        continue
    break

expense_list = []
balance_list = []
loan_list = []

expense_count = 0
done = False

while not done:
    expense_count += 1
    if expense <= balance:
        balance = balance - expense
        print("ATTENTION \n Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, the loan is {loan_balance}:")
    elif expense <= balance + loan_balance:
        print("WARNING \n You don't have enough balance, the purchase will be done from your active loan balance.")
        debt = balance - expense
        loan_balance -= abs(debt)
        balance = 0
        print("ATTENTION \n Purchase has been done successfully!")
        print(f"{full_name}'s current balance after {expense_count} purchase is: {balance}, and the loan is: {loan_balance}")
    else:
        print(f"WARNING \nYour expense [{expense}] is more than your fund: [loan:{loan_balance} + balance:{balance}].")
        print("The purchase couldn't be done.")
        break
    expense_list.append(expense)
    balance_list.append(balance)
    loan_list.append(loan_balance)

    while True:
        next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower()
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
            print("Invalid input. Please enter 'yes' or 'no'. ")

print(f"_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement ")
if len(balance_list) == 0:
    print("No purchase has been done. Thank you for using Budget Tracker.")
else:
    count = min(len(expense_list), len(balance_list), len(loan_list))
    for i in range(count):
        print(f"{i+1}) Expense: {expense_list[i]}, Balance: {balance_list[i]}, Loan: {loan_list[i]}.")





