from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them

    using parse(), and return the contents as a list of list of cells."""

    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()
    lines = f.readlines()
    f.close()
    return parse(lines)


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    #  Transform the input into a nested list which can be changed
    grid = [list(line.strip()) for line in lines]

    char = {' ': 0, 'X': 0, 'Y': 0, '*': 0, 'F': 0, 'W': 0,
            '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            c = str(grid[i][j])
            #  Invalid cases
            if c not in char:
                raise ValueError("Bad letter in configuration file: {}.".format(c))
            else:
                char[c] += 1
                #  initial the objects
                #  The purpose of initializing the coordinates of each object
                #  is to establish the adjacency list in solver.py
                if c == ' ':
                    grid[i][j] = Air()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c == 'X':
                    grid[i][j] = Start()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c == 'Y':
                    grid[i][j] = End()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c == '*':
                    grid[i][j] = Wall()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c == 'F':
                    grid[i][j] = Fire()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c == 'W':
                    grid[i][j] = Water()

                    grid[i][j].x = i
                    grid[i][j].y = j
                elif c in '123456789':
                    grid[i][j] = Teleport()
                    #  change the attribute
                    teleport = grid[i][j]
                    teleport.display = int(c)

                    grid[i][j].x = i
                    grid[i][j].y = j

    #  other invalid cases
    if char['X'] != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(char['X']))

    if char['Y'] != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(char['Y']))

    for t in '123456789':
        if char[t] != 2 and char[t] != 0:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(t))

    return grid

