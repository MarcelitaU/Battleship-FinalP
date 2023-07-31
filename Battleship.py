import random

DIR = ['Right', 'Left', 'Up', 'Down']

def create_grid(coordinates: list) -> list:
    # Function to create a 10x10 grid and place ships at the given coordinates
    grid = [['.' for i in range(10)] for j in range(10)]

    for i in coordinates:
        X = i[0]
        Y = i[1]
        grid[X][Y] = 'X'

    return grid

def ship_position(size: int, dir: str, X: int, Y: int) -> list:
    # Function to determine the positions of the ship based on size and direction
    XY = []

    for s in range(0, int(size)):
        if dir == 'Down':
            XY.append((X + s, Y))
        if dir == 'Up':
            XY.append((X - s, Y))
        if dir == 'Right':
            XY.append((X, Y + s))
        if dir == 'Left':
            XY.append((X, Y - s))
        if dir == 0:
            XY.append((X, Y))
    return XY

def validity(XY: list, coordinates: list) -> bool:
    # Function to check if the ship positions are valid (not overlapping and within the grid)
    valid = True
    for pos in XY:
        if pos in coordinates:
            print('There is already a ship in this position')
            valid = False
            break

        if pos[0] > 9 or pos[1] > 9 or pos[0] < 0 or pos[1] < 0:
            print('Ship is positioned out of the grid')
            valid = False
            break
    return valid

def init_grid_player(n_ships: int) -> list:
    # Function to initialize the player's grid by asking for ship positions
    coordinates = []
    i = 0
    while i < n_ships:
        position = input(f'insert position for ship number {i + 1}: ')
        X = int(position[1])
        Y = int(position[3])

        valid_size = False
        while not valid_size:
            size = input(f'insert size for ship number {i + 1}: ')
            try:
                if int(size) >= 1 and int(size) < 4:
                    valid_size = True
                else:
                    print(f'\terror: size must be a number between 1 and 3')
            except ValueError:
                print(f'\terror: size must be a number')

        if int(size) > 1:
            valid_dir = False
            while not valid_dir:
                dir = input(f'insert direction for ship number {i + 1}: ')
                if dir in DIR:
                    valid_dir = True
                else:
                    print(f'\terror: position must be one of {DIR}')
        else:
            dir = 0

        XY = ship_position(size, dir, X, Y)
        valid = validity(XY, coordinates)
        if valid:
            for pos in XY:
                coordinates.append(pos)
            i += 1

    grid = create_grid(coordinates)
    for line in grid:
        print(line)
    return coordinates, grid

def init_grid_pc(n_ships: int) -> list:
    # Function to initialize the computer's grid by randomly placing ships
    coordinates = []
    i = 0
    while i < n_ships:
        i += 1
        X = random.randint(0, 9)
        Y = random.randint(0, 9)

        size = random.randint(1, 3)
        if size > 1:
            dir = random.choice(DIR)
        else:
            dir = 0

        XY = ship_position(size, dir, X, Y)
        valid = validity(XY, coordinates)

        if valid:
            for pos in XY:
                coordinates.append(pos)
        else:
            i -= 1

    grid = create_grid(coordinates)

    return coordinates, grid

def attack_coo_pc():
    # Function to generate random attack coordinates for the computer
    X = random.randint(0, 9)
    Y = random.randint(0, 9)
    return X, Y

def attack_coo_player():
    # Function to get attack coordinates from the player
    position = input('Insert attack coordinates: ')
    X = int(position[1])
    Y = int(position[3])
    return X, Y

def attack(grid: list, X: int, Y: int) -> list:
    # Function to handle the attack and update the grid
    if grid[X][Y] == 'X':
        print('ship hit')
        grid[X][Y] = '.'
    else:
        print('ship not hit')

    return grid

def count_ships(grid: list) -> int:
    # Function to count the remaining ships on the grid
    sum = 0
    for line in grid:
        sum = sum + line.count('X')

    return sum

def main():
    # Main function to run the game
    n_ships = 2

    init_coo_player, grid_player = init_grid_player(n_ships)
    init_coo_pc, grid_pc = init_grid_pc(n_ships)
    print(init_coo_pc)

    win = False

    while win is False:
        # Player attack
        x, y = attack_coo_player()
        grid_pc = attack(grid_pc, x, y)

        pc_ships = count_ships(grid_pc)
        print(pc_ships)

        # PC attack
        x, y = attack_coo_pc()
        grid_player = attack(grid_player, x, y)

        player_ships = count_ships(grid_player)
        print(player_ships)

        if player_ships == 0:
            win = True
            print('PC has won')
        if pc_ships == 0:
            win = True
            print('Player has won')

if __name__ == "__main__":
    main()