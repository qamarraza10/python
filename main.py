# Input Function (Built-in-Function) to get input value from the user
# To get data type and use of if else statement for float numbers and string input from user
# Use of multiple "If statement"
# To clean_up the code
# Nested if_else statements
# Error handling with try/except or try/caught by removing the user input validation statement
# Value Error Handling, but if we remove ValueError word it will be handling all the type of errors
# While loop to make program continue
# While loop to stop the continues program when the user want to stop it
# Loop is executing the function with same logic multiple times and number of times depends upon the condition
# For Loop is used to iterating over a sequence, we can execute something for item in a list
# Sets data type (as with lists, used to store multiple items of data, does not allow duplicate values)
# Dictionary data type (Used to store values in key:value pairs, Is a collection, which doesn't allow duplicate values)
# Modules (Note: Logically organize the Python code, Module should contain related code)
# Module is a python file that contain function and variables that can be used in another python file, and we can reference one module in other
# Importing specific function from a module
from helper import validate_and_execute # defining in this main.py file module there is a module named helper.py and we are importing a specific function from it
user_input = "" # assigning an empty string to user_input to declare and pass the user input variable in
# while loop to exit the program when user wants to stop
while user_input != "exit": # this have two things here, 1st is a conditional in a loop, 2nd is negative equal check for values
    user_input = input("Hi, Please enter number of days and conversion e.g. 20:hours or 10:minutes :") # input() function is always treated as string and not a number
    days_and_unit = user_input.split(":") # split user input in two values as a list
    print(days_and_unit)
# {"days": 20, "unit": "hours"} # syntax of dictionary, In dictionary we have description for each of our values represented as key value pairs.
# as this is a data type so we can create a value and assign it to a variable
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    # in this {"days": days_and_unit[0]} getting value for days from the days_and_unit list and accessing first element of list
    # To access the specific value in dictionary days_and_unit_dictionary["days"], we are accessing this by keyname
# So, now we have two pieces of information ["days": days_and_unit[0], "unit": days_and_unit[1]] in one variable  [days_and_unit_dictionary]
# and we can give that variable to our function for validation
    validate_and_execute(days_and_unit_dictionary)
    # In order to make this dictionary available in validate and execute function we are passing it as a variable in validate_and_execute function call
    # and also in function named validate_and_execute in the helper file module
    # Note that in main.py module file we only need the validate and execute function we don't need the days and units function
    # as this function is only used in the validate and execute function

