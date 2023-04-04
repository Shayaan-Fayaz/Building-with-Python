import random
import string

def generate_password(min_length, is_numbers=True, is_special = True):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    characters = letters
    if is_numbers:
        characters += numbers
    if is_special:
        characters += special

    pwd = ""

    meet_criteria = False
    has_number = False
    has_special =  False

    while not meet_criteria or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in numbers:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria=True
        if is_numbers:
            meet_criteria =has_number
        if is_special:
            meet_criteria=meet_criteria and has_special

    return pwd


min_length = int(input("What is the minimum length of your password: "))
is_number = input("Do you want numbers? (y/n): ")=='y'
is_special =input("Do you want special characters? (y/n): ")=='y'

password = generate_password(min_length, is_number, is_special)
print(password)