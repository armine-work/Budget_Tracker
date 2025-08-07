#################################################################### get valid number from user
def get_number(user_input, error_ms):
    while True:
        user_input_number = input(user_input).strip()
        if user_input_number.replace(".", "", 1).isnumeric():
            user_input_number = float(user_input_number) if '.' in user_input_number else int(user_input_number)
            return user_input_number
        else:
            print(error_ms)

################################################################## remove extra spaces and get full name
def get_full_name(name, surname):
    full_name = name.title() + " " + surname.title()
    full_name_split = full_name.split()
    full_name = " ".join(full_name_split)
    return full_name
    #print("full name is", full_name)