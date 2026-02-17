# practice projects chapter 4 page 102
def format_list(list):
    """return a neatly formatted string"""
    message = ""
    last = list[-1]
    for item in list:
        if item == last:
            message += f"and {item}."
        else:
            message += f"{item}, "
    return message


# function call
items = ['apples', 'bananas', 'tofu', 'cats']
print(format_list(items))

# character picture grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
# turn around to print it with loops, but how ??
# print(grid[0][0])
# print(grid[1][0])
# print(grid[2][0])
# print(grid[3][0])
column = 0
row = 0

while row <= 5:
    column = 0
    while column <= 8:
       # list [][]
        print(f"{grid[column][row]}", end="")
        column += 1
    row += 1
    print()

# it fucking works yay!
