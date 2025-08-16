import logging
logger = logging.getLogger(__name__)

#################################################################### get valid number from user
def get_number(user_input, error_ms):
    while True:
        user_input_number = input(user_input).strip()
        if user_input_number.replace(".", "", 1).isnumeric():
            user_input_number = float(user_input_number) if '.' in user_input_number else int(user_input_number)
            return user_input_number
        else:
            print(error_ms)
            logger.error(f"incorrect input from user: [{user_input_number}]")
            #############

################################################################## remove extra spaces and get full name
def get_full_name(name, surname):
    full_name = name.title() + " " + surname.title()
    full_name_split = full_name.split()
    full_name = " ".join(full_name_split)
    #print("full name is", full_name)
    logger.debug(f"full name after formatting: [{full_name}]")
    ############
    return full_name



