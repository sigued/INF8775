#!/usr/bin/env python3


import heapq
import time
from typing import List

# Python program to solve
# Gold Mine problem

MAX = 100


# Returns maximum amount of
# gold that can be collected
# when journey started from
# first column and moves
# allowed are right, right-up
# and right-down
def getMaxGold(gold, m, n):
    # Create a table for storing
    # intermediate results
    # and initialize all cells to 0.
    # The first row of
    # goldMineTable gives the
    # maximum gold that the miner
    # can collect when starts that row
    goldTable = [[0 for i in range(n)]
                 for j in range(m)]

    for row in range(n):
        for col in range(m):

            # Gold collected on going to
            # the cell on the rigth(->)
            if (row == 0):
                left = 0
                mid = 0
                right = 0
            elif (col - 1 < 0 and row > 0):
                left = 0
                mid = goldTable[row - 1][0]
                right = goldTable[row - 1][1]
            elif (col == m - 1 and row > 0):
                left = goldTable[row - 1][col - 1]
                mid = goldTable[row - 1][col]
                right = 0
            else:
                left = goldTable[row - 1][col - 1]
                mid = goldTable[row - 1][col]
                right = goldTable[row - 1][col + 1]


            # Max gold collected from taking
            # either of the above 3 paths
            goldTable[row][col] = gold[row][col] + max(mid, left, right)



    #construction du path
    rows, cols = (goldTable.index(max(goldTable, key=max)), 2)
    index_tab = [[0 for i in range(cols)] for j in range(rows+1)]
    col_of_max = (goldTable[goldTable.index(max(goldTable, key=max))])
    index_tab[rows][0] = index_tab[rows][1] = col_of_max.index(max(col_of_max))

    for i in range(rows-1, -1, -1):
        if index_tab[i+1][0] - 1 < 0:
            index_tab[i][0] = 0
        else:
            index_tab[i][0] = index_tab[i+1][0] - 1

        if index_tab[i+1][1] + 1 >= m - 1:
            index_tab[i][1] = m - 1
        else:
            index_tab[i][1] = index_tab[i+1][1] + 1




    # The max amount of gold
    # collected will be the max
    # value in first column of all rows
    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])

    return res, goldTable, index_tab

if __name__ == '__main__':
    gold = [[-1, 47, 81, -3, 21, 15],
            [0, 0, 0, 0, -30, -1],
            [-3, 321, -1, 53, -1, 0],
            [0, 537, -3, -3, 2, -1],
            [-5, 0, 0, 40, 320, 0],
            [-2, -2, 28, 450, -5, -5]]

# Driver code

    # gold = [[1, 3, 1, 5],
    #         [2, 2, 4, 1],
    #         [5, 0, 2, 3],
    #         [0, 6, 1, 2]]

    # m = 6
    # n = 6
    # res, goldTable, ind = getMaxGold(gold, m, n)
    # print(goldTable)
    # print(ind)
    # tab = (goldTable[goldTable.index(max(goldTable, key=max))])
    # print((tab.index(max(tab))))
    lst = [[-1, 47, 81, -3, 21, 15], [47, 81, 81, 81, -9, 20], [78, 402, 80, 134, 80, 20], [402, 939, 399, 131, 136, 79], [934, 939, 939, 439, 456, 136], [937, 937, 937, 138, 451, 451]]
    print(lst.index(max(lst, key=max)))
    # print(res)

# This code is contributed
# by Soumen Ghosh.
