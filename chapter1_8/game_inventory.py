inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(dictionary):
    total_amount = 0
    print ('Inventory:')
    for key, value in dictionary.items():
        print(str(value) + ' ' + str(key))
        total_amount = total_amount + value
    print('Total number of items: ' + str(total_amount))

def add_to_inventory(dictionary, addeditems):
    for index, item in enumerate(addeditems):
        if item not in dictionary.keys():
            dictionary[item] = 1
        else:
            dictionary[item] = dictionary[item] + 1

add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
