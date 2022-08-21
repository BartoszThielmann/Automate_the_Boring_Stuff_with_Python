from pathlib import Path
import re

content_list=[]
p = Path('C:/Users/Bartosz/Documents/Programming/programs/Automate_the_Boring_Stuff_with_Python/chapter9/regex_search_files')
for index, item in enumerate(list(p.glob('*.txt'))):
    content = open(item, 'r+').readlines()
    for index, item in enumerate(content):
        content_list.append(item)
print(content_list)

print('What would you like to find?')
user_search = input()
regex=re.compile(user_search)

for index, item in enumerate(content_list):
    try:
        if regex.search(item).group() == user_search:
            print(item)
    except AttributeError:
        print('')
