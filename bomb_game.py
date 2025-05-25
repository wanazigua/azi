import sys


# create map grid
def create_grid(n):
    grid = []
    for i in range(n):
        row = ['x'] * n
        grid.append(row)
    return grid


# create map
def create_map(grid):
    for p in range(len(grid)):
        map = ''
        for q in range(len(grid[p])):
            map += '|' + grid[p][q] + '|'
        print(map)


# get the correct position
def get_valid_input(prompt, grid_size):
    while True:
        try:
            coords = input(prompt).split()
            if len(coords) != 2:
                raise ValueError('Please enter two numbers separated by spaces')

            x, y = map(int, coords)
            if not (0 <= x < grid_size and 0 <= y < grid_size):
                raise ValueError(f'The coordinates must be between 0 and {grid_size - 1}')
            return x, y
        except ValueError as e:
            print(f"Error: {e}")


def game_part(grid):
    n = len(grid)
    print('------Set bomb------')
    x1, y1 = get_valid_input('Player1 set the position of bomb (x y): ', n)
    x2, y2 = get_valid_input('Player2 set the position of bomb (x y): ', n)

    print('-----Game start-----')
    status = True
    while status:
        while True:
            # player 1 put the bomb
            p1, q1 = get_valid_input('Player1 choose one safety position (x y):', n)
            if grid[p1][q1] == '1' or grid[p1][q1] == '2':
                print('This position has been choosed! Please choose another.')
            else:
                break

        # Check whether Player 1 stepped on the bomb
        if p1 == x2 and q1 == y2:
            print('The bomb exploded, player1 lost the game.')
            status = False
            break
        else:
            grid[p1][q1] = '1'
            create_map(grid)

        if not status:
            break

        while True:
            # player 2 put the bomb
            p2, q2 = get_valid_input('Player2 choose one safety position (x y):', n)
            if grid[p2][q2] == '1' or grid[p2][q2] == '2':
                print('This position has been choosed! Please choose another.')
            else:
                break

        # Check whether Player 2 stepped on the bomb
        if p2 == x1 and q2 == y1:
            print('The bomb exploded, player2 lost the game.')
            status = False
            break
        else:
            grid[p2][q2] = '2'
            create_map(grid)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <grid_size>')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError('Grid size must be positive')

    except ValueError as e:
        print(f'Error: {e}')
        sys.exit(1)

    game_map = create_grid(n)
    game_part(game_map)