# write your code here

cells = input('Enter cells: ')
print('---------')
print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
print('---------')


x_win = None
o_win = None
num_of_x = cells.count('X')
num_of_o = cells.count('O')

if cells[0] == cells[1] == cells[2] == 'X' \
        or cells[3] == cells[4] == cells[5] == 'X' \
        or cells[6] == cells[7] == cells[8] == 'X' \
        or cells[0] == cells[4] == cells[8] == 'X' \
        or cells[2] == cells[4] == cells[6] == 'X' \
        or cells[0] == cells[3] == cells[6] == 'X' \
        or cells[1] == cells[4] == cells[7] == 'X' \
        or cells[2] == cells[5] == cells[8] == 'X':
    x_win = True

if cells[0] == cells[1] == cells[2] == 'O' \
        or cells[3] == cells[4] == cells[5] == 'O' \
        or cells[6] == cells[7] == cells[8] == 'O' \
        or cells[0] == cells[4] == cells[8] == 'O' \
        or cells[2] == cells[4] == cells[6] == 'O' \
        or cells[0] == cells[3] == cells[6] == 'O' \
        or cells[1] == cells[4] == cells[7] == 'O' \
        or cells[2] == cells[5] == cells[8] == 'O':
    o_win = True

if x_win is True and o_win is True:
    print('Impossible')
if x_win is None and o_win is None:
    if num_of_o - num_of_x > 1 or num_of_x - num_of_o > 1:
        print('Impossible')
if x_win is None and o_win is None:
    if '_' in cells:
        if num_of_o - num_of_x <= 1 and num_of_x - num_of_o <= 1:
            print('Game not finished')
    else:
        print('Draw')

if x_win is True and o_win is None:
    print('X wins')

if o_win is True and x_win is None:
    print('O wins')
