# builtin functions
# there are so many builtin functions, some of them are these with their syntax

print("any text")
input("enter value")
set([1, 3, 4]) # defining a list in a set, and giving value inside a code without providing anything
int("20")

# Difference in above and below function is that functions above are called directly like that
# but the function bellow has its own set of functions and can be executed like this

list_of_days = user_input.split(", ")
"2, 3".split() #The string here (2, 3) is going to be the parameter of the split and we can also provide an additional parameter
# e.g. the split(", "), we were able to add a comma spce to tell the split function on which character to split the text

# this is type of function called directly on a value, this could be a variable but also string representation.
"text".isdigit() # checks if the string is representation of a digit or just a regular string

# Note: each data type has its own list of functions that can be called on that data type
# FOr demonstration lets take a list and when we enter a dot "." it gives a list of functions that can be performed e.g. remove, add,sort, copy
[1, 3, 4].count()


