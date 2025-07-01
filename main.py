# Create a script that gets the full name, balance, expense, and active loan balance of a customer
# Calculate and print the balance after the expense.
# If the customer spends from the loan, then tell about it
name = input("What is your name? ")
surname = input("What is your surname? ")
full_name = name + " " + surname
#print("The customer's full name is", full_name)
try:
    balance = float(input("What is your balance? "))
    expense = float(input("What is your expense? "))
    loan_balance = float(input("What is your active loan balance? "))
    if expense > 0:
        if balance > 0:
            if expense <= balance:
                current_balance = balance - expense
                print("ATTENTION \n Purchase has been done successfully!")
                print("{fl}'s current balance after purchase is: {cb}, the loan is: {l}".format(fl = full_name, cb=current_balance, l = loan_balance))
            else:
                print("WARNING \n You don't have enough balance, the purchase will be done from your active loan balance.")
                dept = balance - expense
                #print("dept", dept)
                if abs(dept) <= loan_balance:
                    current_loan = loan_balance - abs(dept)
                    print("ATTENTION \n Purchase has been done successfully!")
                    print("{fl}'s current balance after purchase is: {cb}, and the loan is: {l}".format(fl = full_name, cb=dept, l = current_loan))

                else:
                    current_balance = balance
                    print("WARNING \n   Your expense [{ex}] is more than your loan balance [{lb}].".format(ex=expense, lb=loan_balance))
                    print("ATTENTION \n  The purchase couldn't be done.")
                    print("WARNING \n {fl}'s current balance is: {cb}, the loan is: {l}".format(fl=full_name, cb=current_balance, l = loan_balance))
        else:
            print("Your balance is negative, you cannot purchase.")
    else:
        print("{fl}'s current balance is: {cb}, the loan is: {l}".format(fl=full_name, cb=balance, l=loan_balance))
except ValueError:
    print("Please enter a valid number for balance / expense / loan.")