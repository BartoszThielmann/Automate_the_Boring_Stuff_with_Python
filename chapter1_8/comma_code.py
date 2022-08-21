def comma(list1):
    for index, item in enumerate(list1):
        if index < (len(list1)-2):
            print (item + ', ', end='')
        elif index == (len(list1)-2):
            print (item + ' ', end='')
        else:
            print('i ' + item)

spam = []
liczba_przedmiotow = 1
while True:
    print ('Wpisz ' +str(liczba_przedmiotow) + '.' ' przedmiot na listę. Wciśnij l żeby zobaczyć listę. Wciśnij q aby zakonczyc')
    user_input = input()
    if user_input != 'q' and user_input != 'l':
        spam.append(user_input)
        liczba_przedmiotow += 1
    elif user_input == 'l':
        print ('Twoje dotychczasowe przedmioty to: ')
        comma(spam)
    elif user_input == 'q':
        break
print ('Twoja lista to:')
comma (spam)




#spam = ['apples', 'bananas', 'tofu', 'cats']
#comma(spam)
