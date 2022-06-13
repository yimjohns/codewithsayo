# Your country has issued a law that forbids anyone under the age of 18 to vote. You have been asked to write an application that (i) accepts the firstname, lastname, and age of voter, (ii) Determines if the citizen is eligible to vote or not.

first_name = input("What is your first name? ").capitalize()
last_name = input("What is your last name? ").capitalize()
age = int(input("How old are you? "))

if age < 18:
    print(f"Thank you for your interest to vote {last_name} {first_name} but you are NOT eligible to vote!")
else:
    print(f"Thank you for your interest to vote {last_name} {first_name} but you are eligible to vote!")