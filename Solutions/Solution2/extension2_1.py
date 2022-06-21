from timeit import default_timer as timer

from datetime import timedelta

start = timer()


def get_extension(filename):
    return filename.split('.')[-1]

file_name = input("Enter file name: ")

f_extension = get_extension(file_name)

if f_extension == 'txt':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as Text file.")
elif f_extension == 'java':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as Java file.")
elif f_extension == 'py':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as Python file.")
elif f_extension == 'c':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as C file.")
elif f_extension == 'js':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as JavaScript file.")
elif f_extension == 'cs':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as CSharp file.")
elif f_extension == 'doc':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as Document file.")
elif f_extension == 'xlsx':
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as Excel file.")
else:
    print('That file exension does not exists in our database!')
end = timer()

print(f'Time elapsed {timedelta(seconds=end - start)}')