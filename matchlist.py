def grade(score):
    match score:
        case [20, 20, 30]:
            return "Found"
        case _:
            return "Not Found"


print(f"{grade(20)}")



