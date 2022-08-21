# Jak jest dużo casow to lepiej switcha uzyc - Mikolaj Zelek

import random, sys
print ('ROCK, PAPER, SCISSORS')

win = 0
loss = 0
tie = 0
print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')

while True:

    print ('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    gracz = str(input())
    if gracz == 'r':
        gracz = 'ROCK'
    elif gracz == 'p':
        gracz = 'PAPER'
    elif gracz == 's':
        gracz = 'SCISSORS'
    elif gracz == 'q':
        sys.exit()
    else:
        print ('Co ty klikasz chlopie')
        continue

    komputer = random.randint (1, 3) #zamienic na random.choice
    if komputer == 1:
        komputer = 'ROCK'
    elif komputer == 2:
        komputer = 'PAPER'
    elif komputer == 3:
        komputer = 'SCISSORS'

    print (str(gracz) + ' versus...')
    print (komputer)

    if gracz == komputer:
        tie = tie + 1 #zamienic na +=
        print ('It is a tie!')
        print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
    elif gracz == 'ROCK' and komputer == 'SCISSORS':
        win = win + 1 #zamienic na +=
        print ('You win!')
        print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
    elif gracz == 'PAPER' and komputer == 'ROCK':
        win = win + 1 #zamienic na +=
        print ('You win!')
        print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
    elif gracz == 'SCISSORS' and komputer == 'PAPER':
        win = win + 1 #zamienic na +=
        print ('You win!')
        print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
    else:
        loss = loss + 1 #zamienic na +=
        print('You lost!')
        print (str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
