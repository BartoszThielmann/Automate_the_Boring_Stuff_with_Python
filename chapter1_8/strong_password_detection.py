#! python3
# strong_password_detection.py - Determines if a password is strong.

import re

while True:
    counter = 0
    print('Check your password strength! Give me your password:')
    password = input()

    #check if password has at least eight characters
    password_length_regex = re.compile(r'\w{8,}')
    mo = password_length_regex.search(password)
    if not mo == None:
        counter += 1

    #check if password has at least one digit
    password_digit_regex = re.compile(r'\d')
    mo = password_digit_regex.search(password)
    if not mo == None:
        counter += 1

    #check if password contains uppercase
    password_digit_regex = re.compile(r'[A-Z]')
    mo = password_digit_regex.search(password)
    if not mo == None:
        counter += 1

    #check if password contains lowercase
    password_digit_regex = re.compile(r'[a-z]')
    mo = password_digit_regex.search(password)
    if not mo == None:
        counter += 1

    if counter == 4:
        print('Strong password!')
    else:
        print('Weak!')
