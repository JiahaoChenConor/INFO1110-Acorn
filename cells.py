class Start:
    def __init__(self):
        self.display = 'X'
        self.x = 0
        self.y = 0

    def step(self, game):
        pass

class Air:
    def __init__(self):
        self.display = ' '
        self.x = 0
        self.y = 0

    def step(self, game):
        pass

class Wall:
    def __init__(self):
        self.display = '*'
        self.x = 0
        self.y = 0

    #  Go back
    def step(self, game):
        game.player.row -= game.dx
        game.player.col -= game.dy

        sentence = "\nYou walked into a wall. Oof!"
        game.moves.pop()
        game.movesNum -= 1
        return [sentence, 'continue']

class Water:
    def __init__(self):
        self.display = 'W'
        self.x = 0
        self.y = 0

    # Take away the current water, the element at this coordinate becomes an object of Air
    def step(self, game):
        game.grid[game.player.row][game.player.col] = Air()
        sentence = "\nThank the Honourable Furious Forest, you've found a bucket of water!"
        game.player.num_water_buckets += 1
        return [sentence, 'continue']

class Teleport:
    def __init__(self):
        self.display = 0
        self.x = 0
        self.y = 0

    def step(self, game):
        #  Find the other teleport which has the same number
        for i in range(game.row):
            for j in range(game.column):
                if game.grid[i][j].display == game.cell.display and game.grid[i][j] != game.cell:
                    game.player.row = i
                    game.player.col = j
        sentence = "\nWhoosh! The magical gates break Physics as we know it" \
                   " and opens a wormhole through space and time."
        return [sentence, 'continue']



class Fire:
    def __init__(self):
        self.display = 'F'
        self.x = 0
        self.y = 0

    def step(self, game):
        #  Enough water
        if game.player.num_water_buckets > 0:
            game.grid[game.player.row][game.player.col] = Air()
            sentence = "\nWith your strong acorn arms, you throw a water bucket at the fire. "  \
                       "You acorn roll your way through the extinguished flames!"
            game.player.num_water_buckets -= 1
            return [sentence, 'continue']

        #  Lack of water
        else:
            sentence = "\n\nYou step into the fires and watch your dreams disappear :(.\n"  \
                       "\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of "  \
                       "ash and is scattered to the winds by the next storm... You have been roasted.\n\n"  \
                       "You made {} moves.\n".format(game.movesNum) + \
                       "Your moves: {}\n\n".format(', '.join(game.moves)) + \
                       "=====================\n"  \
                       "===== GAME OVER =====\n"  \
                       "====================="
            return [sentence, 'fail']


class End:
    def __init__(self):
        self.display = 'Y'
        self.x = 0
        self.y = 0

    def step(self, game):
        if game.movesNum != 1:
            sentence = "\n\nYou conquer the treacherous maze set up by the Fire Nation and "  \
                       "reclaim the Honourable Furious Forest Throne, "  \
                       "restoring your hometown back to its former glory of rainbow and sunshine! "  \
                       "Peace reigns over the lands."  \
                       "\n\nYou made {} moves.".format(game.movesNum) + \
                       "\nYour moves: {}".format((', '.join(game.moves)).lower()) + \
                       "\n\n====================="  \
                       "\n====== YOU WIN! ====="  \
                       "\n====================="
        else:
            sentence = "\n\nYou conquer the treacherous maze set up by the Fire Nation and "  \
                       "reclaim the Honourable Furious Forest Throne, "  \
                       "restoring your hometown back to its former glory of rainbow and sunshine! "  \
                       "Peace reigns over the lands."  \
                       "\n\nYou made {} move.".format(game.movesNum) + \
                       "\nYour move: {}".format((', '.join(game.moves).lower())) + \
                       "\n\n====================="  \
                       "\n====== YOU WIN! ====="  \
                       "\n====================="

        return [sentence, 'success']









