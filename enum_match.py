from enum import Enum

class Color(Enum):
    RED = 'red'.lower()
    GREEN = 'green'.lower()
    BLUE = 'blue'.lower()


color = Color(input("Enter a color of your choice: red, green, or blue: "))

match color:
    case color.RED:
        print("Roses are Red too!")
    case color.GREEN:
        print("The grass is green!")
    case color.BLUE:
        print("The sky is quite blue!")



