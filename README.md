# Budget_Tracker  

Initialize a Python project in PyCharm called Budget Tracker  .
⦁	Create a script called main.py.  
⦁	Create a script that gets the full name, balance, expense, and active loan balance of a customer.  
⦁	Calculate and print the balance after the expense.  
⦁	If the customer spends from the loan, then tell about it  
⦁	Do necessary checks.  
⦁	Print in a readable and nice format.  

feature_refactor(branch)  
⦁	Refactor code to use at least two types of data structures for working with data.  
⦁	For example: Expenses as a dictionary, Initial balances as tuples.  
⦁	With string operation, make better formatting for customer name, like removing extra spaces, and make capitalized name parts.  
⦁	For each transaction, create a transaction ID in this format name.surname-id and store them in the data structure for transactions.  

feature_files_data_input (branch)  
• Add a new input value that will check if the name, balance and loan will be provided manually or from a file  
•  If Yes, the program should work as before (in terms of input)  
•  If No, the program should read data from a file called “CustomerData”.    
   File path must be an additional input.  
   Input file one line: Name, Surname, balance, loan  
•  Write transactions in to a file called “Transaction.txt”  

feature_modules (branch)  
• Create functions for the code (repeated codes and logical units must be in functions)  
• Create module(s) and/or packages for those functions  

feature_logging (branch)  
• Add logs for all print functions, and store them in separate file.  
  
feature_classes (branch)  
• Create a PersonBudget class with its constructor, attributes, and methods  
• All input info: name, balance, and loan must be stored in the class object  
• Transaction must be stored in the class objects as well  
• Note: getting customer's data from file on manually input is out of scope for this PR  
