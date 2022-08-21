import re
import pyperclip

months_max_30 = ['04', '06', '09', '11']
months_max_31 = ['01', '03', '05', '07', '08', '10', '12']

day=[]
month=[]
year=[]

user_input = str(pyperclip.paste())
date_regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9]{3})(\s|\.)+')
mo = date_regex.findall(user_input)

for index, item in enumerate(mo):
    if ((mo[index][1] in months_max_30) and (int(mo[index][0]) <= 30) and (int(mo[index][0]) > 0)):
        day.append(mo[index][0])
        month.append(mo[index][1])
        year.append(mo[index][2])

    elif ((mo[index][1] in months_max_31) and (int(mo[index][0]) <= 31) and (int(mo[index][0]) > 0)):
        day.append(mo[index][0])
        month.append(mo[index][1])
        year.append(mo[index][2])

    elif ((mo[index][1] == '02') and (int(mo[index][0]) <= 28) and (int(mo[index][0]) > 0)):
        day.append(mo[index][0])
        month.append(mo[index][1])
        year.append(mo[index][2])

    elif ((mo[index][1] == '02') and int(mo[index][0]) == 29 and (int(mo[index][2])%4==0 or int(mo[index][2])%400==0)):
        day.append(mo[index][0])
        month.append(mo[index][1])
        year.append(mo[index][2])

if len(day) == 0:
    print('Nie znaleziono dat')

for index, item in enumerate(day):
    print('Znalezione daty: ')
    print(item + '/' + month[index] + '/' + year[index])



