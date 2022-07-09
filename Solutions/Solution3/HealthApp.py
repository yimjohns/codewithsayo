import random
import sys


def main():
    user = input(greetings_msg())
    interact_with(user.capitalize())


def interact_with(user, prompt_greetings=None):
    prompts = [
        'How can I help you today?',
        'glad to have you around today. How can I help you?'
    ]
    if prompt_greetings is not None:
        prompt(user, prompt_greetings)
    else:
        prompt(user, prompts)
    get_input(user)


def greetings_msg():
    return random.choice(
        (
            'May I know your name please?',
            'Hello, may I know your name, please?',
            'Thank you for being here, what is your name please?'
        )
    )


def prompt(user, prompt_texts):
    welcome_message = f'Welcome {user.capitalize()}'

    prompt_text = random.choice(prompt_texts)
    prompt_text = f"{welcome_message}, {prompt_text}"
    prompt_text += '''
        Enter 1 if you wish to get a list of approved COVID vaccines 
        Enter 2 if you wish to determine your proneness to COVID
        Enter 0 to quit
    '''
    print(prompt_text)


def get_input(user):
    choices = {0: quit_app, 1: get_list_of_vaccines, 2: determine_proneness}
    while True:
        try:
            choice = int(input())
            if choice in choices.keys() and choice != 0:
                action = choices.get(choice)
                action()
                continue_app(user)
                break
            elif choice == 0:
                quit_app(user)
            send_message(user)
            sys.exit()
        except Exception as err:
            send_message(user, err)


def get_list_of_vaccines():
    print("As of today, the approved list of COVID vaccines are (list them here...)")


def determine_proneness():
    print("This service isn't available yet, please check again later.")


def quit_app(user):
    quit_msgs = (
        'Do have a wonderful day.',
        'See you again some other time.',
        'Do have a wonderful day ahead of you.'
    )
    print(f"Thank you for your time, {user}! {random.choice(quit_msgs)}")

    sys.exit()


def send_message(user, error=None):
    if error:
        print(f"An Exception Occurred: {error}")
    print(f"Sorry, {user} but I don't understand what you just typed in. \nIf you don't mind trying again")
    # prompt(user)
    interact_with(user)


def continue_app(user):
    prompt_messages = (
        'Thank you for staying with us! What more would you like us to do for you?',
        'Glad to have you stick with us! What else would you like us to do for you?',
        'Happy still to have you around! What else would you like use to do for you?'
    )
    while True:
        continue_prompt = input("Do you wish to continue? - Y for Yes, N for No")
        if continue_prompt.lower() == 'y':
            interact_with(user, prompt_messages)
            break
        elif continue_prompt.lower() == 'n':
            quit_app(user)
            break
        print("The response entered is not valid! - Please try again")


if __name__ == "__main__":
    main()
