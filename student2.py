def main():
    name = get_name()
    city = get_city()

    print(f"{name} lives in {city}")


def get_name():
    return input("What is the Student's name? ")


def get_city():
    return input("In what City does the Student live? ")

if __name__ == "__main__":
    main()
