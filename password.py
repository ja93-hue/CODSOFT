#This is a simple password generator application in python
#It allows user to specify the length of the password and whether user wants to include
# uppercase letters, lowercase letters, digits, and special characters

import random
import string

def password_generator(length, upper_case, lower_case, digits, special_char):
    print('x')
    character = " "
    if upper_case:
        character = character + string.ascii_uppercase
    if lower_case:
        character = character + string.ascii_lowercase
    if digits:
        character = character + string.digits
    if special_char:
        character = character + string.punctuation

    if not character:
     raise ValueError("Atleat one character set must be selected")

    password = ''.join(random.choice(character) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    upper_case = input("Include upper case letters? yes/no: ").strip().lower() == "yes"
    lower_case =  input("Include lower case letters? yes/no: ").strip().lower() == "yes"
    digits = input("Include digits? yes/no: ").strip().lower() == "yes"
    special_char = input("Include special characters? yes/no: ").strip().lower() == "yes"

    try:
        password = password_generator(length, upper_case, lower_case, digits, special_char)
        print(f"password generated: {password}")
     
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
