#! python3
# Write a program that asks users for their sandwich preferences.
# The program should use PyInputPlus to ensure that they enter valid input

import pyinputplus as pyip

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'What kind of bread?\n')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'What kind of protein?\n')
cheese = pyip.inputYesNo('Do you want cheese?(yes/no)\n')
if cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
else:
    cheese_type = 'None'
additional = pyip.inputYesNo('Do you want an additional ingredient?(yes/no)\n')
if additional == 'yes':
    additional_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
else:
    additional_type = 'None'
amount = pyip.inputInt('How many sandwiches do you want?\n', min=1)

prices = {'wheat': 2, 'white': 2, 'sourdough': 3, 'chicken': 2, 'turkey': 3, 'ham': 1, 'tofu': 2,
'cheddar': 2, 'Swiss': 3, 'mozzarella': 5, 'mayo': 1, 'mustard': 1, 'lettuce': 3, 'tomato': 3, 'None': 0}

total = amount * (prices[bread] + prices[protein] + prices[cheese_type] + prices[additional_type])

print('Order summary:\n Bread: %s \n Protein: %s \n Cheese: %s \n Additional: %s \n Amount: %s \n Price: %s$' %
(bread, protein, cheese_type, additional_type, amount, total))
