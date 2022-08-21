def collatz():
        global number
        if number % 2 == 0:
            number = number // 2
            return print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            return print(number)
while True:
    try:
        number = int(input())
        while number != 1:
            collatz()
    except ValueError:
        print ('You must enter an integer')
