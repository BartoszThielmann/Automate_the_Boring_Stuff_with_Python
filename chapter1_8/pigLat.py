print('Enter the English message to translate into Pig Latin:')
message = ('My name is AL SWEIGART and I am 4,000 years old.')
message_split = message.split()
for i in enumerate(message_split):
    if str(i[0]).lower() == 'a':
        i[0] = '%'


print(message_split)
