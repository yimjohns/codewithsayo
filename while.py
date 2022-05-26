student_names = []

while True:
    print(f'Enter the name of student {(len(student_names) + 1)} or enter nothing to stop: ')
    name = input()

    if not name:
        break