# Command-line arguments: n, m, pFish, pShrimp, pMountain where
# n, m - amount of rows and columns of a field, pX - probability that X will appear (for every cell)

import argparse
import os
import time
import random

none, fish, shrimp, mountain = ' ', 'F', 'S', '#'

class Life:
    field = []
    def __init__(self, _field):
        self.field = _field
    def nextState(self): # returns the next state of the field
        f = self.field
        nextField = f
        for i in range(len(f)):
            for j in range(len(f[0])):
                fishCount, shrimpCount = 0, 0
                for dr in range(i - 1, i + 2):
                    for dc in range(j - 1, j + 2):
                        if (0 <= dr and dr < len(f) and
                            0 <= dc and dc < len(f[dr]) and
                            not (i == dr and j == dc)):
                                if f[dr][dc] == fish:
                                    fishCount += 1
                                elif f[dr][dc] == shrimp:
                                    shrimpCount += 1
                if f[i][j] == none:
                    if fishCount == 3:
                        nextField[i][j] = fish
                    elif shrimpCount == 3:
                        nextField[i][j] = shrimp
                elif f[i][j] == fish:
                    if fishCount <= 1 or 4 <= fishCount:
                        nextField[i][j] = none
                elif f[i][j] == shrimp:
                    if shrimpCount <= 1 or 4 <= shrimpCount:
                        nextField[i][j] = none
        return nextField

    def __str__(self):
        s = ""
        for i in self.field:
            for j in i:
                s += j
            s += "\r\n"
        return s

class LifeFactory:
    @staticmethod
    def makeRandomLife(rowsCount, colsCount, pFish, pShrimp, pMountain):
        field = [[none for j in range(colsCount)] for i in range(rowsCount)]
        for i in range(rowsCount):
            for j in range(colsCount):
                r = random.random()
                if r < pFish:
                    field[i][j] = fish
                elif r < pFish + pShrimp:
                    field[i][j] = shrimp
                elif r < pFish + pShrimp + pMountain:
                    field[i][j] = mountain
        return Life(field)

def clearScreen(): # clears screen
    if os.name == 'nt': # windows
        _ = os.system('cls')
    else: # linux/mac
        _ = os.system('clear')

parser = argparse.ArgumentParser()
parser.add_argument('rowsCount', help='Amount of rows',    type=int)
parser.add_argument('colsCount', help='Amount of columns', type=int)
parser.add_argument('-pf', '--pFish',     help='Probability that fish will appear',     type=float)
parser.add_argument('-ps', '--pShrimp',   help='Probability that shrimp will appear',   type=float)
parser.add_argument('-pm', '--pMountain', help='Probability that mountain will appear', type=float)
parser.add_argument('-n', '--none',     help='symbol for "none" symbol in map')
parser.add_argument('-f', '--fish',     help='symbol for "fish" symbol in map')
parser.add_argument('-s', '--shrimp',   help='symbol for "shrimp" symbol in map')
parser.add_argument('-m', '--mountain', help='symbol for "mountain" symbol in map')
args = parser.parse_args()

pFish     = args.pFish     if args.pFish     != None else 0.2
pShrimp   = args.pShrimp   if args.pShrimp   != None else 0.3
pMountain = args.pMountain if args.pMountain != None else 0.1
if pFish + pShrimp + pMountain > 1:
    raise(ValueError('Sum of probabilities is more than 1'))

none     = args.none     if args.none     else ' '
fish     = args.fish     if args.fish     else 'F'
shrimp   = args.shrimp   if args.shrimp   else 'S'
mountain = args.mountain if args.mountain else '#'

life = LifeFactory.makeRandomLife(args.rowsCount, args.colsCount, pFish, pShrimp, pMountain)

clearScreen()
print('Initial state:')
print(life)
time.sleep(0.5)

stateTurn = 1
while True:
    clearScreen()
    life = Life(life.nextState())
    print('State #' + str(stateTurn) + ':')
    print(life)
    time.sleep(0.1)
    stateTurn += 1
