#!/usr/bin/env python3


import heapq
from typing import List


# code inspirée de https://github.com/dennyzhang/code.dennyzhang.com/tree/master/problems/the-skyline-problem
def getSkyline(buildings: List[List[int]]):
    points = []
    for i, b in enumerate(buildings):
        points.append([b[0], -b[2]])  # start
        points.append([b[1], b[2]])  # end
    points.sort()
    tempList = []
    # add a dummy height to avoid hitting the ground
    heapq.heappush(tempList, 0)
    maxH = 0
    skylineTable = []
    for p in points:
        if p[1] < 0:
            # push the close point
            heapq.heappush(tempList, p[1])
        else:
            # close current range
            for i, v in enumerate(tempList):
                if v == -p[1]:
                    del tempList[i]
                    heapq.heapify(tempList)
                    break
        # peek
        if len(tempList) > 0 and maxH != tempList[0]:
            maxH = tempList[0]
            skylineTable.append([p[0], -maxH])
    return skylineTable

#
# if __name__ == "__main__":
#     result = getSkyline([(2, 9, 10), (3, 7, 15), (5, 12, 12), (15, 20, 10),
#                          (19, 24, 8)
#                          ])
#     print(result)
