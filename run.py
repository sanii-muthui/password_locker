#!/usr/bin/env python3.7
from user import User
from credential import Credential


def create_user(email, password):
    """
    Function to create a new user
    """
    new_user = User(email, password)
    return new_user


def create_credential(pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credential(pword, email)
    return new_credential


def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()


def save_cred(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()


def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


def del_cred(credential):
    """
    Function to delete all users credentials
    """
    credential.delete_credential()


def display_user():
    """
    Function that returns saved users
    """
    return User.display_users()


def display_cred():
    """
    function that returns saved user credentials
    """
    return Credential.display_credential()


def main():

    print("Welcome to your Password Locker,Select an Option:")

    while True:
        print("Options: \n 1. - create a new user account and password\n"
              " 2. - create a new user account with a auto-generated password\n"
              " 3. - display all user accounts \n"
              " 4. - exit the account list \n")

        options = int(input())

        if options == 1:
            print("New User")
            print("Please create a site for your account!")
            site = input()
            print(f" {site} created!Welcome")

            print("Enter Your email account")
            e_address = input()

            print("Enter password ...")
            e_password = input()

            save_user(create_user(e_address, e_password))  # create and save new user account.
            save_cred(create_credential(e_password, e_address)) # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {e_address} has successfully been created")
            print(f" The email is {e_address} and the password is {e_password}")
            print('\n')

        elif options == 2:
            print("New User")
            print("Please create a site for your account!")
            site = input()
            print(f"{site} created!Welcome")

            print("Enter Your email account ...")
            e_address = input()

            print("Enter password ...")
            e_password = input()

            save_user(create_user(e_address, e_password))  # create and save new user account.
            save_cred(create_credential(e_password, e_address))  # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {e_address} has successfully been created")
            print(f" The username is {e_address} and the password is {e_password}")
            print('\n')

        elif options == 3:

            if display_user():
                print("Here is a list of all your user accounts")
                print('\n')

                for user in display_user():
                    print(f"{user.email} has an account for {site}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any existing accounts")
                print('\n')

        elif options == 4:
            print(":/ YOU ARE EXITING PASSWORD LOCKER...")
            break
        else:
            print(" :( please enter selected options!!")


if __name__ == '__main__':
    main()