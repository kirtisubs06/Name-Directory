from database import Simpledb

db = Simpledb('directory.txt')


def add():
    name = input("What is the name that you would like to add? ")
    number = input("What is that person's number? ")
    db.insert(name, number)


def find():
    name = input("What is the name that you would like to find? ")
    db.select_one(name)


def delete():
    name = input("What is the name that you would like to delete? ")
    db.delete(name)


def update():
    name = input("What is the name of the contact that you would like to update? ")
    db.update(name)


while True:
    command = input(
        "What would you like to do today? (enter a for add, f for find, d for delete, u for update, or q for quit): ")
    if command == "a":
        add()
    elif command == "f":
        find()
    elif command == "d":
        delete()
    elif command == "u":
        update()
    elif command == "q":
        break
    else:
        print("Please enter a valid command. ")
