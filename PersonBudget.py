import logging
logging.basicConfig(
                    level = logging.DEBUG,
                    filename = 'logs.txt',
                    format = '%(levelname)s - %(message)s - %(filename)s - %(asctime)s ',
                    datefmt = '%H:%M:%S %m-%d-%Y',
                    filemode = 'w' )
from app.validation_check import get_number, get_full_name


class PersonBudget:
    def __init__(self, name, surname, balance, loan_balance):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.loan_balance = loan_balance
        self.transactions_data = []

################################################################# calculate balance after expense
    def balance_calculator(self, expense, full_name):
        expense_count = 0
        done = False

        while not done:
            expense_count += 1
            if expense <= self.balance:
                self.balance = self.balance - expense
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self.balance}, the loan is {self.loan_balance}:")
                logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {self.balance}, the loan is {self.loan_balance}:")
                ###########
            elif expense <= self.balance + self.loan_balance:
                print("You don't have enough balance, the purchase will be done from your active Loan Balance.")
                debt = self.balance - expense
                self.loan_balance -= abs(debt)
                self.balance = 0
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self.balance}, and the loan is: {self.loan_balance}")
                logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {self.balance}, and the loan is: {self.loan_balance}")
                ############
            else:
                print(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self.loan_balance} + balance:{self.balance}].")
                print("The purchase couldn't be done. Closing the program")
                logging.warning(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self.loan_balance} + balance:{self.balance}].")
                ###############
                break
            ##################################################################### create expenses ID after each transaction
            username = full_name.replace(" ", ".")
            expense_id = username.lower() + "-" + str(expense_count)
            #print(f"{full_name} customer's expense ID is {expense_id}.")
            logging.debug(f"{full_name} customer's expense ID is {expense_id}.")
            ############

            #################################################################### store data in dictionary
            self.transactions_data.append({
                "expense": expense,
                "balance": self.balance,
                "loan_balance": self.loan_balance,
                "expense_id": expense_id
            })
            ##################################################################### ask for a new expense
            while True:
                next_expense_prompt = input("Would you like to do another expense? (yes/no) ").lower().strip()
                logging.debug(f"next expense prompt: [{next_expense_prompt}]")
                #############
                if next_expense_prompt == "yes":
                    expense = get_number(user_input="What's customer's new expense? ",
                                         error_ms="Please enter numeric, positive value for expense: ")
                    logging.debug(f"new expense: [{expense}]")
                    #############
                    break
                elif next_expense_prompt == "no":
                    print("Thank you. The purchase process is finished.")
                    logging.info("The purchase process is finished.")
                    ###########
                    done = True
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    logging.error(f"wrong input from user [{next_expense_prompt}]")
                    ############

    def print_transactions(self, full_name):
        print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
        if len(self.transactions_data) == 0:
            print("No purchase has been done. Thank you for using Budget Tracker.")
            logging.info("No purchase has been done.")
            ############
        else:
            for i, transaction in enumerate(self.transactions_data, start=1):
                print(f"{i}) Expense: {transaction['expense']}, "
                      f"Balance: {transaction['balance']}, Loan: {transaction['loan_balance']}."
                      f"\nExpense ID is: {transaction['expense_id']}")
                logging.debug(f"Expense: {transaction['expense']}, "
                      f"Balance: {transaction['balance']}, Loan: {transaction['loan_balance']}."
                      f"Expense ID is: {transaction['expense_id']}")
                #############
