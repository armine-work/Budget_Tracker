# import logging
# logger = logging.getLogger(__name__)

from app.validation_check import get_number

############################################################################# get expense from user 
def get_expense(user_input):
    expense = get_number(user_input, error_ms="Please enter numeric, positive value for expense: ")
    return expense