from timeit import default_timer as timer

from datetime import timedelta

start = timer()
file_extensions = {
    'txt':'Text',
    'java':'Java',
    'py': 'Python',
    'c': 'C',
    'js': 'JavaScript',
    'cs': 'CSharp',
    'doc': 'Document',
    'xlsx': 'Microsoft Excel'
}

print(file_extensions['xlsx'])

def get_extension(filename):
    return filename.split('.')[-1]

file_name = input("Enter file name: ")
f_extension = get_extension(file_name)

if f_extension in file_extensions.keys():
    f_ext_category = file_extensions[f_extension]
    print(f"The file name '{file_name} with the file extension '{f_extension}' can be categorised as {f_ext_category} file.")
else:
    print(f"The file type for '{file_name}' isn't recognized!")
end = timer()

print(f'Time elapsed {timedelta(seconds=end - start)}') # Time elapsed 0:00:19.628683