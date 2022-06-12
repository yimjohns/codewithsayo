def main():
    name, city = get_student()
    print(f"{name} lives in {city}")


def get_student():
    name = input("What is the Student's name? ")
    city = input("In what City does the Student live? ")

    return name, city


if __name__ == "__main__":
    main()

