def main():
    student = get_student()
    if student[0].capitalize() == 'Johnson':
        student[1] = 'Abuja'
    print(f"{student[0]} lives in {student[1]}")


def get_student():
    name = input("What is the Student's name? ")
    city = input("In what City does the Student live? ")

    # Return a tuple which could explicitly be returned using Parenthesis () return (name, city)
    return name, city


if __name__ == "__main__":
    main()
