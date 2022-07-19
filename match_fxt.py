def main():
    filename = input("Enter the file name: ")
    f_ext = get_extension(filename) # txt
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = "The file is " + ("an" if f_ext[0].lower() in vowels else "a")
    print(f"{output} {f_ext} file")


def get_extension(filename):
    match filename.split('.')[-1]:
        case 'txt':
            return 'Text'
        case 'java':
            return 'Java'
        case 'py':
            return 'Python'
        case 'c':
            return 'C'
        case 'js':
            return 'JavaScript'
        case 'cs':
            return 'CSharp'
        case 'doc' | 'docx':
            return 'Document'
        case 'xlsx' | 'xls':
            return 'Excel'
        case _:
            return 'Unknown'


if __name__ == "__main__":
    main()