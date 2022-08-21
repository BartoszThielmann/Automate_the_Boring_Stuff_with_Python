table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


test_table_data = ['apples', 'oranges', 'cherries', 'banana']

def printTable(data):
    longest_in_column =[0] * len(data)
    for y in range(len(data[0])):
        for x in range(len(data)):
            if len(data[x][y]) > longest_in_column[x]:
                longest_in_column[x] = len(data[x][y])

    for y in range(len(data[0])):
        for x in range(len(data)):
            print (data[x][y].rjust(longest_in_column[x]), end=' ')
        print()

    print(longest_in_column)

printTable(table_data)
