#! python3
#mad libs program

import re

text_file = open('madlibs_text.txt', 'r+')
text_file_content = text_file.read()
text_file_content_split = text_file_content.split()
for index,item in enumerate(text_file_content_split):
    if 'VERB' in item:
        print('Enter a verb:')
        user_input = input()
        word_regex = re.compile(r'VERB')
        text_file_content_split[index] = word_regex.sub(user_input, text_file_content_split[index])
    elif 'NOUN' in item:
        print('Enter a noun:')
        user_input = input()
        word_regex = re.compile(r'NOUN')
        text_file_content_split[index] = word_regex.sub(user_input, text_file_content_split[index])
    elif 'ADJECTIVE' in item:
        print('Enter an adjective:')
        user_input = input()
        word_regex = re.compile(r'ADJECTIVE')
        text_file_content_split[index] = word_regex.sub(user_input, text_file_content_split[index])
print(' '.join(text_file_content_split))
text_file.close()

text_file = open('altered_madlibs_text.txt', 'w')
text_file.write(' '.join(text_file_content_split))
text_file.close()
