# 3. Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, we have a list of names as defined here – names = [‘John’, ‘James’, ‘Betty’, ‘Bobby’]. Passing the names list to the function would return ‘John, James, Betty, and Bobby. But your function should be able to work with any list value passed to it.
# Hint: The function is defined as follow:

# def sep_with_comma(my_list):
#        # Your code goes here…

# sep_with_comma(original_list)

def sep_with_comma(my_list):
    spam_copy = my_list[: -1]

    print(', '.join(spam_copy) + ', and ' + my_list[-1])

# Test the function
fruits = ['Apple', 'Orange', 'Banana', 'Cherry']

sep_with_comma(fruits)