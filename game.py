from game_parser import read_lines
from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.moves = []
        self.movesNum = 0
        self.player = Player()
        self.grid = read_lines(filename)
        self.row = len(self.grid)
        self.column = len(self.grid[0])

    #  Record valid input(path)
    def gameMove(self, move):
        self.moves.append(move)

    #  Put the player on the starting position
    def setStart(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j].display == 'X':
                    self.player.row = i
                    self.player.col = j

    #  Update player location and map information based on input
    def coordinateUpdate(self, move, game):
        #  Quit the game
        if move == 'q' or move == 'Q':
            return 'quit'

        if move not in ['w', 'W', 's', 'S', 'a', 'A', 'd', 'D', 'q', 'Q', 'e', 'E']:
            sentence = "\nPlease enter a valid move (w, a, s, d, e, q)."
            return [sentence, 'continue']

        change = self.player.move(move)
        self.dx, self.dy = change[0], change[1]
        self.player.row += self.dx
        self.player.col += self.dy
        self.movesNum += 1
        self.gameMove(move)

        #  If player want to get out of the map, treat this behavior as hitting a wall
        if self.player.row < 0 or self.player.row > len(self.grid) - 1 or \
            self.player.col < 0 or self.player.col > len(self.grid[self.player.row]) - 1:
            sentence = "\nYou walked into a wall. Oof!"
            self.player.row -= self.dx
            self.player.col -= self.dy
            self.moves.pop()
            self.movesNum -= 1
            return [sentence, 'continue']
        else:
            self.cell = self.grid[self.player.row][self.player.col]
            return self.cell.step(game)

    #  Update the grid based on the updated map and player information
    def updateGrid(self):
        #  temp is the updated grid
        #  list1 = list2 will not create a new list
        #  temp = copy.deepcopy(self.grid) if import copy

        #  I need to use the original grid every time
        temp = [[self.grid[i][j] for j in range(self.column)] for i in range(self.row)]
        temp[self.player.row][self.player.col] = self.player
        return temp

    def showGrid(self):
        temp = self.updateGrid()
        output = grid_to_string(temp, self.player)
        return output

