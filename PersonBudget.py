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
        self._balance = balance
        self._loan_balance = loan_balance
        self.transactions_data = []

################################################################# sett and get functions for Encapsulating all data of the class
        def set_balance(self, balance):
            self._balance = balance

        def get_balance(self):
            return self._balance

        def set_loan_balance(self, loan_balance):
            self._loan_balance = loan_balance

        def get_loan_balance(self):
            return self._loan_balance


################################################################# calculate balance after expense
    def balance_calculator(self, expense):
        full_name = get_full_name(self.name, self.surname)
        
        expense_count = 0
        done = False

        while not done:
            expense_count += 1
            if expense <= self._balance:
                self._balance = self._balance - expense
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, the loan is {self._loan_balance}:")
                logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, the loan is {self._loan_balance}:")
                ###########
            elif expense <= self._balance + self._loan_balance:
                print("You don't have enough balance, the purchase will be done from your active Loan Balance.")
                debt = self._balance - expense
                self._loan_balance -= abs(debt)
                self._balance = 0
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, and the loan is: {self._loan_balance}")
                logging.info(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, and the loan is: {self._loan_balance}")
                ############
            else:
                print(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self._loan_balance} + balance:{self._balance}].")
                print("The purchase couldn't be done. Closing the program!")
                logging.warning(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self._loan_balance} + balance:{self._balance}].")
                ###############
                break
            ##################################################################### create expenses ID after each transaction
            username = full_name.replace(" ", ".")
            expense_id = username.lower() + "-" + str(expense_count)
            #print(f"{full_name} customer's expense ID is {expense_id}.")
            logging.debug(f"{full_name} customer expense ID is: {expense_id}.")
            ############

            #################################################################### store data in dictionary
            self.transactions_data.append({
                "expense": expense,
                "balance": self._balance,
                "loan_balance": self._loan_balance,
                "expense_id": expense_id
            })
            ##################################################################### ask for a new expense
            while True:
                next_expense_prompt = input("\nWould you like to do another expense? (yes/no) ").lower().strip()

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


    def print_transactions(self):
        full_name = get_full_name(self.name, self.surname)

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

class OnlineBudget(PersonBudget):
    def __init__(self, name, surname, balance, loan_balance, online_loan):
        super().__init__(name, surname, balance, loan_balance)
        self.__online_loan = online_loan

    def set_online_loan(selfself, online_loan):
        __online_loan = online_loan
    def get_pnline_loan(self):
        return self.__online_loan


    def balance_calculator(self, expense):
        full_name = get_full_name(self.name, self.surname)
        
        expense_count = 0
        done = False

        while not done:
            expense_count += 1
            if expense <= self._balance:
                self._balance = self._balance - expense
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, the loan is {self._loan_balance}:")
                logging.info(f"Expense {expense_count}, Balance: {self._balance}, Loan: {self._loan_balance}:")
                ###########
            elif expense <= self._balance + self._loan_balance:
                print("You don't have enough balance, the purchase will be done from your active Loan Balance.")
                debt = self._balance - expense
                self._loan_balance -= abs(debt)
                self._balance = 0
                print("\n___ATTENTION___ Purchase has been done successfully!")
                print(f"{full_name}'s current balance after {expense_count} purchase is: {self._balance}, and the loan is: {self._loan_balance}")
                logging.info(f"Expense {expense_count}, Balance: {self._balance}, Loan: {self._loan_balance}")
                ############

            elif expense <= self._balance + self._loan_balance + self.__online_loan:
                print(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self._loan_balance} + balance:{self._balance}].")
                logging.warning(f"{full_name}'s expense [{expense}] is more than funds: [loan:{self._loan_balance} + balance:{self._balance}].")
                ###############
                user_input = input("\nDo you want to use online loan? (yes/no) ").strip().lower()
                logging.debug(f"Prompt for online loan: [{user_input}]")
                if user_input == "yes":
                    debt = self._loan_balance - expense
                    self.__online_loan -= abs(debt)
                    self._loan_balance = 0
                    print(f"{full_name}'s current balance after {expense_count} purchase is {self._balance}, the loan is: {self._loan_balance}, "
                          f"and the online loan is: {self.__online_loan}")
                    logging.warning(f"Expense: {expense_count}, Balance: {self._balance}, Loan: {self._loan_balance}, Online Loan:{self.__online_loan}")
                    ################
                elif user_input == "no":
                    print("Thank you. The purchase process is finished.")
                    logging.info("The purchase process is finished.")
                    ###########
                    done = True
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    logging.error(f"wrong input from user [{user_input}]")
                    ############

            else:
                print(f"{full_name}'s expense [{expense}] is more than funds: "
                      f"[loan:{self._loan_balance} + balance:{self._balance} + online loan:{self.__online_loan}].")
                logging.warning(f"{full_name}'s expense [{expense}] is more than funds: "
                                f"[loan:{self._loan_balance} + balance:{self._balance} + online loan:{self.__online_loan}].")
                ###############
                print("The purchase couldn't be done. Closing the program!")
                break


            ##################################################################### create expenses ID after each transaction
            username = full_name.replace(" ", ".")
            expense_id = username.lower() + "-" + str(expense_count)
            # print(f"{full_name} customer's expense ID is {expense_id}.")
            logging.debug(f"{full_name} customer expense ID is: {expense_id}.")
            ############

            #################################################################### store data in dictionary
            self.transactions_data.append({
                "expense": expense,
                "balance": self._balance,
                "loan_balance": self._loan_balance,
                "online_loan": self.__online_loan,
                "expense_id": expense_id  })

            ##################################################################### ask for a new expense
            while True:
                next_expense_prompt = input("\nWould you like to do another expense? (yes/no) ").lower().strip()
                logging.debug(f"Prompt for next expense: [{next_expense_prompt}]")
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


    def print_transactions(self):
        full_name = get_full_name(self.name, self.surname)
        print(f"\n_______________FINAL RESULTS_______________ \n {full_name} customer's bank statement:")
        if len(self.transactions_data) == 0:
            print("No purchase has been done. Thank you for using Budget Tracker.")
            logging.info("No purchase has been done.")
            ############
        else:
            for i, transaction in enumerate(self.transactions_data, start=1):
                print(f"{i}) Expense: {transaction['expense']}, "
                      f"Balance: {transaction['balance']}, Loan: {transaction['loan_balance']}, Online Loan: {transaction['online_loan']}."
                      f"\nExpense ID is: {transaction['expense_id']}")
                logging.debug(f"Expense: {transaction['expense']}, "
                      f"Balance: {transaction['balance']}, Loan: {transaction['loan_balance']}, Online loan: {transaction['online_loan']}."
                      f" Expense ID is: {transaction['expense_id']}")
