# Create a script that gets the full name, balance, expense, and active loan balance of a customer
# Calculate and print the balance after the expense.
# If the customer spends from the loan, then tell about it.
# Add one more input, which asks about a new expense. If yes, continue inputting; if no, stop inputting.
# Stop inputting if the customer spends the whole balance and the loan
name = input("What is your name? ")
surname = input("What is your surname? ")
full_name = name + " " + surname
# print("The customer's full name is", full_name)
try:
    balance = float(input("What is your balance? "))
    loan_balance = float(input("What is your active loan balance? "))
    expense = float(input("What is your expense? "))
    # checking person's balance after first purchase
    if loan_balance > 0:
        if balance > 0:
            if expense > 0:
                expense_count = 1
                if expense <= balance:
                    balance_1 = balance - expense
                    print("ATTENTION \n Purchase has been done successfully!")
                    print(f"{full_name}'s current balance after {expense_count} purchase is: {balance_1}, the loan is {loan_balance}:")
                # elif expense == balance:
                #     balance_1 = balance - expense
                #     print("ATTENTION \n Purchase has been done successfully!")
                #     print(f"{full_name}'s current balance after {expense_count} purchase is [0]: {balance_1}, the loan is {loan_balance}:")
                else:
                    print("WARNING \n You don't have enough balance, the purchase will be done from your active loan balance.")
                    dept_1 = balance - expense
                    # print("dept", dept)
                    if abs(dept_1) <= loan_balance:
                        loan_balance_1 = loan_balance - abs(dept_1)
                        balance_1 = 0
                        print("ATTENTION \n Purchase has been done successfully!")
                        print(f"{full_name}'s current balance after purchase is: {balance_1}, and the loan is: {loan_balance_1}")

                    else:
                        balance_1 = balance
                        loan_balance_1 = loan_balance
                        print(f"WARNING \nYour expense [{expense}] is more than your loan balance [{loan_balance_1}].")
                        print("The purchase couldn't be done.")

                while True:
                    next_expense_prompt = input("Would you like to do another expense? ").lower()
                    if next_expense_prompt == "yes":
                        expense_count += 1
                        new_expense = float(input("What is your new expense? "))
                        if new_expense > 0:
                            if new_expense <= balance_1:
                                print("ATTENTION \n Purchase has been done successfully!")
                                balance_2 = balance_1 - new_expense

                                print(f"{full_name}'s current balance after {expense_count} purchases is: {balance_2}, the loan is {loan_balance}")
                                balance_1 -= new_expense
                            else:
                                print("WARNING \n You don't have enough balance, the purchase will be done from your active loan balance.")
                                dept_2 = balance_1 - new_expense
                                # print("dept_2", dept_2)
                                if abs(dept_2) <= loan_balance:
                                    loan_balance_2 = loan_balance - abs(dept_2)
                                    balance_2 = 0

                                    print("ATTENTION \n Purchase has been done successfully!")
                                    print(f"{full_name}'s current balance after {expense_count} purchases is: {balance_2}, and the loan is: {loan_balance_2}")
                                    loan_balance -= abs(dept_2)

                                else:
                                    balance_2 = balance_1
                                    loan_balance_2 = loan_balance
                                    print(f"WARNING \nYour new expense [{new_expense}] is more than your loan balance [{loan_balance_2}].")
                                    print("The purchase couldn't be done.")
                                    break
                        else:
                            print("Please enter positive value for the 'new expense'. ")

                    elif next_expense_prompt == "no":
                        print("Ok, thank you.")
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no' ")
            else:
                print("Please enter positive value for 'expense' ")
        else:
            print("Please enter positive value for the 'balance' ")
    else:
        print("Please enter positive value for the 'loan balance' ")

except ValueError:
    print("Please enter a valid number for balance / expense / loan.")