#! regex_strip.py

# Write a function that takes a string and does the same thing as the strip() string method.
#If no other arguments are passed other than the string to strip,
#then whitespace characters will be removed from the beginning and end of the string.
#Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re

def regex_strip(string):
    input_regex = re.compile(r'([^ ])(.*)([^ ])')
    mo = input_regex.search(string)
    print(mo.groups())

regex_strip('    takie zdanie   ')
