#! python3
#! Character_picture_grid.py - from chapter 4 ATBS

# Character picture grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('\n'.join(map(''.join, zip(*grid)))

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('')
