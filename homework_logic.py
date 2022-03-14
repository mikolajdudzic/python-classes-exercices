from optparse import Option
from db_homework import *

users = {}

def sign_up(_username, _password, _db):
    if len(_password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    users[_username] = _password
    print("You now have an account!")

def sign_in(_username, _password, _db):
    if users[_username] == _password:
        print("Your're logged in")
    else:
        print("incorrect login or password, please try again...")
    

while True:
    print("1. Sign up")
    print("2. Sign in")
    print("3. Exit")
    option = input("Select an option: ")
    if option == "1":
        username = input("Username: ")
        password = input("Password: ")
        sign_up(username, password, users)
        cursor.execute(f'INSERT INTO users VALUES ("{username}"", "{password}"')
    elif option == "2":
        username = input("Username: ")
        password = input("Password: ")
        sign_in(username, password, users)
    elif option == "3":
        print("Bye")
        break