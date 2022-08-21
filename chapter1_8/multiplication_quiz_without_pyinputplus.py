#! python3
# multiplication quiz without PyInputPlus

import time, random
correct_answer = 0
for question_number in range(1,4):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    print('Question #' + str(question_number) + ' What is ' + str(num1) +'*'+ str(num2))

    start = time.time()
    for tries in range(0,3):
        try:
            answer = int(input())
            if answer == num1*num2:
                break
            else:
                print('Try again!')
        except ValueError:
            print('Input a integer!')
            answer = None
            continue
    end = time.time()

    if answer == num1*num2 and end-start < 8:
        print('Good job! Answer time: ' + str(end-start))
        correct_answer += 1
        time.sleep(1)
    elif answer != num1*num2:
        print('Wrong answer')
    elif end-start >= 8:
        print('Too slow!')

print('Your score is: ' + str(correct_answer) + '/3')
