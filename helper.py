def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return (f"{num_of_days} days are {num_of_days * 24} hours")
    elif conversion_unit == "minutes":
        return (f"{num_of_days} days are {num_of_days * 24 * 60} minutes")
    else:
        return "Unsupported unit"

# To clean_up the code for best practice in functions
def validate_and_execute(days_and_unit_dictionary): # function to validate the user input by try and except block to handle multiple errors

    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
          calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
          print(calculated_value)
        elif user_input_number == 0:
            print ("You entered a zero, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number!")

