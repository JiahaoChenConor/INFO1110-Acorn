"""
Author: Jiahao Chen (Conor)
Date: 10 May 2020
Purpose: Implement a small game 'Acorn Runner'
License: USYD Open Source License.
"""

from game import Game
import os
import sys


def run_game():
    # Correct command arguments
    if len(sys.argv) == 2:
        #  show the grid at first
        game = Game(sys.argv[1])
        game.setStart()
        print(game.showGrid())

        while True:
            move = input("\nInput a move: ")
            state = game.coordinateUpdate(move, game)

            if state == 'quit':
                print('\nBye!')
                sys.exit()

            print(game.showGrid())
            if state != None:
                print(state[0])
                if state[1] == 'continue':
                    continue
                elif state[1] in ['success', 'fail']:
                    break

    #  Wrong length of command arguments
    else:
        print("Usage: python3 run.py <filename> [play]")
        exit()


run_game()
