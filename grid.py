def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    #  according to the row and column, put player instance into the grid
    grid[player.row][player.col] = player

    string = ''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #  attention: teleport's display is an integer
                string += str(grid[i][j].display)
        string += '\n'

    if player.num_water_buckets == 1:
        string += '\n' + 'You have {} water bucket.'.format(player.num_water_buckets)
    else:
        string += '\n' + 'You have {} water buckets.'.format(player.num_water_buckets)

    return string



