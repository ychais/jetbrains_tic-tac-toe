# the beginning of the game
cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
print('---------')
print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
print('---------')


# current state of the game
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
not_finished = False

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
            not_finished = True
    else:
        print('Draw')

if x_win is True and o_win is None:
    print('X wins')

if o_win is True and x_win is None:
    print('O wins')


# turn to insert

repeat = True
space = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
i_chosen_cell = 0
if not_finished:
    while repeat:
        print('Enter the coordinates: ')
        x, y = input().split()
        x = int(x)
        y = int(y)
        coord = str(x) + str(y)
        if coord in space:
            if x == 1:
                if y == 1:
                    i_chosen_cell = 0
                elif y == 2:
                    i_chosen_cell = 1
                elif y == 3:
                    i_chosen_cell = 2
            elif x == 2:
                if y == 1:
                    i_chosen_cell = 3
                elif y == 2:
                    i_chosen_cell = 4
                elif y == 3:
                    i_chosen_cell = 5
            elif x == 3:
                if y == 1:
                    i_chosen_cell = 6
                elif y == 2:
                    i_chosen_cell = 7
                elif y == 3:
                    i_chosen_cell = 8
            cells = list(cells)
            if cells[i_chosen_cell] != '_':
                print('This cell is occupied! Choose another one!')
                repeat = True
            else:
                cells.pop(i_chosen_cell)
                cells.insert(i_chosen_cell, 'X')
                print('---------')
                print('| ' + cells[0] + ' ' + cells[1] + ' ' + cells[2] + ' |')
                print('| ' + cells[3] + ' ' + cells[4] + ' ' + cells[5] + ' |')
                print('| ' + cells[6] + ' ' + cells[7] + ' ' + cells[8] + ' |')
                print('---------')
                repeat = False

        elif x < 1 or x > 3 or y < 1 or y > 3:
            print('Coordinates should be from 1 to 3!')
            repeat = True
        else:
            print('You should enter numbers!')
            repeat = True
