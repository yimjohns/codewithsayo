from ast import match_case


def http_error(status_code):
    match status_code:
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 418:
            return 'Just another error!'
        case 500:
            return 'Internal Server Error!'
        case _:
            return "Something might just be wrong with the internet"


def main():
    error_code = int(input("What is the error code? "))
    print(f"{http_error(error_code)}")


if __name__ == "__main__":
    main()
