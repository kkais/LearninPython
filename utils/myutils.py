# import only system from os
from os import system, name


# define our clear function
def clear():
    # print(name)

    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def append_to_file(file, item):
    file_handle = open(file, "a")

    if file_handle.writable():
        data = item
        file_handle.write(item)
    else:
        data = "Error in reading file: " + file

    file_handle.close()

    return data


def read_file(file):
    file_handle = open(file, "r")

    if file_handle.readable():
        data = file_handle.readlines()
    else:
        data = "Error in reading file: " + file

    file_handle.close()

    return data
