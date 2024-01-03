# Can only access the elements of a set in a loop e.g. For Loop
# In basic set operations we can create, access only by loop, add an item, remove an items
# Item in a set don't have a defined order, cannot be referred by index,items can't be changed, only add & remove

my_set = {"Jan", "Feb", "March"} # creating a set
for element in my_set: # for loop to access the elements of set
    print(element)

my_set.add("April") # the new added element is added randomly in set
print(my_set)

my_set.remove("Jan") # removing an element in a set
print(my_set)

my_list = ["Jan", "Feb", "March", "Jan"] # creating a list with duplicate values
my_list.remove("Jan") # In list it removes the 1st present value from the duplicate values
print(my_list)




