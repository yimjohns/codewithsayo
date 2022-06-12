# def do_something_else():
#     pass

# def do_something():
#     return ("I'm doing something here...")


# if __name__ == "__main__":
#     print("We got in here!")
#     do_me = do_something
#     print(do_me)

# def get_username(username):
#     return username.lower()

# def authenticate(user):
#     if user == get_username(user):
#         print("Yipee! You're in!")
#     else:
#         print("Oops! Sorry, you're an intruder!")


# def area_of_rectangle(length, breadth):
#     return length*breadth

# authenticate("Johnson")

def authenticate_user(email, password):
    if email == "sayo@gmail.com" and password == "123456":
        print("You have successfully logged in!")
    else:
        print("Invalid login detail!")


def get_user_input():
    email = input("What is your email? ")
    password = input("What is your password? ")

    print(f"The Email supplied by the user is {email} and the password is {password}")
    
    authenticate_user(email, password)


get_user_input()