from app.file_usage import get_data_from_file, write_data_to_file
from app.expense_input import get_expense
from app.validation_check import get_number, get_full_name

############################################################### calculate balance after each expense 
#                                                               and store the results in appropriate list/dictionary

def balance_calculator(expense, balance, loan_balance, full_name, expenses_sheet, balances_list):
    
    expense_count = 0
    done = False
    
    while not done:
        expense_count += 1
        if expense <= balance:
            balance = balance - expense
            print("___ATTENTION___ Purchase has been done successfully!")
            print(
                f"{full_name}'s current balance after {expense_count} purchase is: {balance}, the loan is {loan_balance}:")
        elif expense <= balance + loan_balance:
            print(
                "___WARNING___ You don't have enough balance, the purchase will be done from your active loan balance.")
            debt = balance - expense
            loan_balance -= abs(debt)
            balance = 0
            print("___ATTENTION___ Purchase has been done successfully!")
            print(
                f"{full_name}'s current balance after {expense_count} purchase is: {balance}, and the loan is: {loan_balance}")
        else:
            print(
                f"___WARNING___ Your expense [{expense}] is more than your funds: [loan:{loan_balance} + balance:{balance}].")
            print("The purchase couldn't be done.")
            break
            
        ##################################################################### create expenses ID after each transaction

        space_count = full_name.count(" ")
        username = full_name.replace(" ", ".")
        expense_id = username.lower() + "-" + str(expense_count)
        # print(f"{full_name} customer's expense ID is {expense_id}.")

        #####################################################################armi store expenses in dictionary
        expenses_data = {"expense_count": expense,
                         "expense_id": expense_id}
        ##################################################################### convert expenses data to a list
        expenses_sheet.append(expenses_data)
        ##################################################################### store balance with loan balance in a tuple
        balances_tuple = tuple((balance, loan_balance))
        ##################################################################### convert balance data to a list, so it can be added more
        balances_list.append(balances_tuple)
        
        ##################################################################### call writing transaction function

        write_data_to_file(expenses_sheet, balances_list, full_name)
        ##################################################################### ask for a new expense
        while True:
            next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower().strip()
            if next_expense_prompt == "yes":
                expense = get_expense("What is user's new expense? ")
                # print("new expnese", expense)
                break
            elif next_expense_prompt == "no":
                print("Ok, thank you. The purchase process is finished.")
                done = True
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")