from utils.myutils import *


def show_menu():
    clear()
    print("1. Type your name to see it in reverse")
    print("2. Show Todo list")
    print("3. Add a Todo")
    print("4. Remove a Todo")
    print("0. Exit program")


def reverse_name():
    clear()
    user_name = input("Enter your name: ")
    print("Name: " + user_name)
    print("Reverse Name: " + user_name[::-1])  # prints the name in reverse using string slicing
    print("*************************")


def show_list(list):
    clear()
    print("************ TODO LIST *************")
    for item in list:
        print(item)
    print("************ END OF TODO LIST *************")


def add_item(file, item):
    append_to_file(file, item)


def read_list(file):
    data = read_file(file)
    if data:
        for item in data:
            print(item)




