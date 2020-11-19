class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0

    def move(self, move):
        if move == 'w' or move == 'W':
            return [-1, 0]

        elif move == 's' or move == 'S':
            return [1, 0]

        elif move == 'a' or move == 'A':
            return [0, -1]

        elif move == 'd' or move == 'D':
            return [0, 1]

        elif move == 'e' or move == 'E':
            return [0, 0]





