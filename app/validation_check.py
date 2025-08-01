#################################################################### get valid number from user
def get_number(user_input, error_ms):
    while True:
        user_input_number = input(user_input).strip()
        if user_input_number.replace(".", "", 1).isnumeric():
            user_input_number = float(user_input_number) if '.' in user_input_number else int(user_input_number)
            return user_input_number
        else:
            print(error_ms)