# practice project page 142

def print_table(lists):
    """right justify list of lists"""
    # Determine max width for each column
    colWidths = [max(len(word) for word in col) for col in lists]

    for x in range(0, len(lists[0])):
        for i in range(0, len(lists)):
            print(lists[i][x].rjust(colWidths[0]), end=" ")
        print("")


tableData = [['apples', 'oranges', 'bananas', 'cherries'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ]
# function call
print_table(tableData)
