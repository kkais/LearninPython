from core import *

choice = "y"
todo_file = "data/todos.txt"

while choice != 0:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        reverse_name()
    elif choice == 2:
        # show_todo_list(todo_list)
        read_list(todo_file)
    elif choice == 3:
        clear()
        todo = input("Enter your todo item: ")
        add_item(todo_file, todo + "\n")
