# 2. You have been given the ages of students in a class as the following:
# 12, 12, 8, 9, 9, 10, 6, 11.

# Your task is write a program to:
# i.	Find the average age of the students in the class.
# ii.	Determine which age is the highest.
# iii. Determine which age is the lowest. 

class_age = 12, 12, 8, 9, 9, 10, 6, 11

total = 0
highest = lowest = class_age[0]

for i in class_age:
    total += i
    highest = i if (i > highest) else highest
    lowest = i if (i < lowest) else lowest

print(f'The average age of the students is {total / len(class_age)}')

print(f"The highest age is {highest}")

print(f"The lowest age is {lowest}")
