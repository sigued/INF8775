#!/usr/bin/env python3


import heapq
import time
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.res = 0

        def dfs(x, y, gold):
            self.res = max(self.res, gold)
            for (i,j) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0:
                    v = grid[i][j]
                    grid[i][j] = 0
                    dfs(i, j, gold + v)
                    grid[i][j] = v
            print([i, j])

        if grid[0][1] != 0:
            x = grid[0][1]
            grid[0][1] = 0
            # print(x)
            # print(i)
            # print(j)
            dfs(0, 1, x)
            grid[0][1] = x
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] != 0:
        #             x = grid[i][j]
        #             grid[i][j] = 0
        #             # print(x)
        #             # print(i)
        #             # print(j)
        #             dfs(i, j, x)
        #             grid[i][j] = x
        return self.res


if __name__ == '__main__':
    # grid = [[-1, 47, 81, -3, 21, 15],
    #         [0, 0, 0, 0, -30, -1],
    #         [-3, 321, -1, 53, -1, 0],
    #         [0, 537, -3, -3, 2, -1],
    #         [-5, 0, 0, 40, 320, 0],
    #         [-2, -2, 28, 450, -5, -5]]

    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]

    gold_mine = Solution()
    print(gold_mine.getMaximumGold(grid))