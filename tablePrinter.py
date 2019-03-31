#! python3
# tablePrinter.py - Display a list of lists of strings in
# a well-organized table.

table_data =  [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

def print_table(main_arr):
    col_widths = [0] * len(main_arr)

    # Look for largest str length and save it in a column
    for single_arr in main_arr:
        curr_index = main_arr.index(single_arr)
        for string in single_arr:
            if len(string) > col_widths[curr_index]:
                col_widths[curr_index] = len(string)

    # Create a table from array `(x, y)` => `(y, x)`
    table = []
    for x in range(len(main_arr[0])):
        temp_arr = []
        for y in range(len(main_arr)):
            temp_arr.append(main_arr[y][x])
        table.append(temp_arr)
        temp_arr = []

    # Print pretty table
    for arr in table:
        for string in arr:
            str_index = arr.index(string)
            print(string.rjust(col_widths[str_index] + 1), end='')
        print()

print_table(table_data)