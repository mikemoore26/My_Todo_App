from settings import *


def show_list(lis):
    """
    This program takes in a list of todos and display them
    :param lis: List
    :return:
    """
    res = ""
    if not lis:
        res = "The list is currently empty\n"
    else:
        for i, item in enumerate(lis):
            res += f"{i + 1}. {item.title()}"

    print(res, end='')


def remove_item(lis, num, mode):
    """
    Takes in a list and a index number and removes the item in the List
    :param lis: List
    :param num: Int
    :param mode: str
    :return: True is item is successfully removed,
             False if there was an Error
    """
    try:
        temp = lis.pop(num)
        res = f"You {mode} {temp}"
        print(res, end='')
        del temp
        return True
    except IndexError:
        res = "Please enter a valid number"
        print(res)
        return False


def save_todo(lis, filename=FIlENAME):
    """
    Saves list to file

    :param lis: List
    :param filename: str
    :return:
    """
    print("lis", lis)

    with open(filename, 'w') as f:
        f.writelines(lis)


def load_todos(filename=FIlENAME):
    with open(filename, "r") as file:
        todos = file.readlines()
        todos = [todo.title() for todo in todos]

    return todos
