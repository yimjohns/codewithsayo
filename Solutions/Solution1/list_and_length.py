# 4. Write a function that takes a list value and outputs each word in the list and their respective lengths. For example, 
# utensils = ['spoon', 'fork']
# Output:
# Spoon 5
# Fork 4
# Your function should be able to work with any list value passed to it.

def get_list_length(my_list):
    for i in my_list:
        print(i , len(i))


# Test the function
fruits = ['Apple', 'Orange', 'Banana', 'Cherry']
get_list_length(fruits)