from game_parser import read_lines
import sys
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import itertools


#  Adjacency list
class Graph:
    def __init__(self):
        self.vertList = {}

    def addEdge(self, f, t):
        if f not in self.vertList:
            self.vertList[f] = []
        if t not in self.vertList:
            self.vertList[t] = []
        self.vertList[f].append(t)


#  achieve bfs
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#  achieve dfs
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":

    grid = read_lines(sys.argv[1])
    row = len(grid)
    column = len(grid[0])


    def findTheOtherTeleport(grid, i, j):
        for m in range(row):
            for n in range(column):
                if grid[m][n].display == grid[i][j].display and grid[m][n] != grid[i][j]:
                    return grid[m][n]


    def findStart():
        for i in range(row):
            for j in range(column):
                if grid[i][j].display == 'X':
                    start = grid[i][j]

        return start


    def findEnd():
        for i in range(row):
            for j in range(column):
                if grid[i][j].display == 'Y':
                    end = grid[i][j]

        return end

    #  Initialization diagram
    def createDiagram():
        g = Graph()
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        for i in range(row):
            for j in range(column):
                #  This is for the special case when a teleport is surrounded by walls
                if isinstance(grid[i][j].display, int):
                    theOther = findTheOtherTeleport(grid, i, j)
                    g.addEdge(grid[i][j], theOther)
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x <= row - 1 and 0 <= y <= column - 1 and grid[i][j].display != '*' \
                            and grid[x][y].display != '*' and grid[i][j].display != 'Y':
                        if isinstance(grid[x][y].display, int):
                            theOther = findTheOtherTeleport(grid, x, y)
                            g.addEdge(grid[i][j], theOther)
                        else:
                            g.addEdge(grid[i][j], grid[x][y])
        return g

    ## these can check the coordinates in adjacency list
    # g = createDiagram()
    #   for f in g.vertList.keys():
    #     print((f.x,f.y), [(t.x, t.y) for t in g.vertList[f]])

    def judge(cur, next):
        if next[0] - cur[0] == 1 and next[1] == cur[1]:
            return 's'
        elif next[0] - cur[0] == -1 and next[1] == cur[1]:
            return 'w'
        elif next[1] - cur[1] == 1 and next[0] == cur[0]:
            return 'd'
        elif next[1] - cur[1] == -1 and next[0] == cur[0]:
            return 'a'
        else:
            return None

    #  change the coordinates into moves
    def move(track):
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        moves = []
        for i in range(len(track) - 1):
            cur, next = track[i], track[i + 1]
            m = judge(cur, next)
            if m:
                moves.append(m)
            # If the current coordinate and the next coordinate do not satisfy
            # the row coordinate difference 1 or the column coordinate difference 1,
            # there are two possibilities
            else:
                #  1. the next coordinate is teleport
                noWay = True
                for j in range(4):
                    cell = grid[cur[0] + dx[j]][cur[1] + dy[j]]
                    if isinstance(cell.display, int):
                        next = [cell.x, cell.y]
                        m = judge(cur, next)
                        moves.append(m)
                        noWay = False

                #  2. the current coordinate is teleport and wait because there is no way except teleport
                if noWay == True:
                    moves.append('e')
        return moves

    #  judge water or fire, if water + 1, else - 1
    def waterFire(cell):
        if cell.display == 'W':
            return 1
        elif cell.display == 'F':
            return -1
        else:
            return 0


    def dfs(start):
        end = findEnd()
        g = createDiagram()
        stack = Stack()

        water = 0
        water += waterFire(start)

        # Record the valid path
        track = []
        stack.push(start)
        coordinate = (start.x, start.y)
        track.append(coordinate)

        # Record the points that have been passed
        searched = [start]

        next = None
        while not stack.isEmpty():
            #  if I change cur, it will also change stack.items[-1]!!
            cur = stack.items[-1]
            water += waterFire(cur)
            #  if meet water , clear the nodeSet
            if cur.display == 'W':
                searched.clear()
                cur.display = ' '

            #  for-else: If a "break" is executed in the "for" loop, then "else" will not be executed
            for next in g.vertList[cur]:
                if next not in searched:
                    #  check the next node considering the fire
                    water += waterFire(next)
                    if water >= 0:
                        stack.push(next)
                        #  update the track
                        track.append((next.x, next.y))
                        #  this node is already be used
                        searched.append(next)
                        water -= waterFire(next)
                        break
                    water -= waterFire(next)

            #  backtrack
            else:
                water -= waterFire(cur)
                stack.pop()
                track.pop()

            #  if reach the end, break the loop
            if next == end:
                break

        return track


    #  First use bfs to find how much fire is needed
    #  Find all water objects stored in the list []
    #  for example, there is three fire on the shortest way to End, and there are five waters on the map
    #  Pick five out of three for full arrangement

    #  Actually it is Brute force + BFS
    def bfs(start, end):
        g = createDiagram()
        queue = Queue()

        queue.enqueue(start)
        #  record the points which have been searched
        searched = [start]

        while not queue.isEmpty():
            cur = queue.dequeue()
            for node in g.vertList[cur]:
                if node not in searched:
                    if node == end:
                        searched.append(node)
                        #  the shortest path
                        path = get_path(searched, g)
                        return path
                    #  if the current point is not the end, enqueue all its adjacent points
                    else:
                        queue.enqueue(node)
                        searched.append(node)
        return []

    #  Find the path
    def get_path(searched, g):
        end = searched[-1]
        path = [(end.x, end.y)]
        while end != searched[0]:
            for i in searched:
                if end in g.vertList[i]:
                    end = i
                    path.append((end.x, end.y))
                    break

        return path[::-1]



    def search():
        global solution_found
        global ans

        if sys.argv[2] == 'DFS':

            track = dfs(findStart())
            ans = move(track)
            solution_found = True

        if sys.argv[2] == 'BFS':

            fireNum = 0
            track = bfs(findStart(), findEnd())
            #  The first bfs, find how many fires in the shortest path
            #  so we can decide how many water we need
            for coord in track:
                if grid[coord[0]][coord[1]].display == 'F':
                    fireNum += 1

            waterObjects = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j].display == 'W':
                        waterObjects.append(grid[i][j])

            #  Is there enough water?
            if fireNum > len(waterObjects):
                solution_found = False
                return

            #  Full arrangement
            comb = list(itertools.permutations(waterObjects, fireNum))

            paths = []
            for waters in comb:
                #  waters is the combination of water objects, such as (water2,  water3, water1)
                start = findStart()
                end = findEnd()
                waters = list(waters)
                waters.append(end)
                path = []

                path += bfs(start, waters[0])

                for i in range(len(waters)-1):
                    start, end = waters[i], waters[i+1]
                    #  If we directly connect the two paths, the coordinates of the water will be repeated，so [1:]
                    path += bfs(start, end)[1:]


                paths.append(path)

            #  Find the shortest path
            shortest = float('inf')
            ans = None
            for way in paths:
                if len(way) < shortest:
                    shortest = len(way)
                    ans = way

            ans = move(ans)
            solution_found = True


    solution_found = False
    ans = []
    search()
    if len(ans) == 0:
        solution_found = False

    if solution_found:
        print("Path has {} moves.".format(len(ans)))
        print("Path: " + ', '.join(ans))
    else:
        print("There is no possible path.")