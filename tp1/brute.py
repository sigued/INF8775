#!/usr/bin/env python3


import heapq
import time
from typing import List


# code inspirée de https://github.com/dennyzhang/code.dennyzhang.com/tree/master/problems/the-skyline-problem

def time_execution_naif(buildings):
    start = time.time()
    getSkyline(buildings)
    end = time.time()
    return (end - start) * 1000


def getSkyline(buildings: List[List[int]]):
    points = []
    for i, b in enumerate(buildings):
        points.append([b[0], b[2]])  # start
        points.append([b[1], -b[2]])  # end
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

# def is_valid(result, new_height):
#     return not result or result[-1][1] != new_height

# def critic_pts(buildings: List[List[int]]):
#     critic_pts = []
#     for building in buildings:
#         critic_pts.extend([[building[0], building[2]]])
#         critic_pts.extend([[building[1], 0]])
#     return critic_pts
#
#
# def brute_algo(buildings: List[List[int]]):
#     points = []
#     for i, b in enumerate(buildings):
#         points.append([b[0], b[2]])  # start
#         points.append([b[1], 0])  # end
#     points.sort()
#     result = []
#     for point in points:
#         h = point[1]
#         for batiment in buildings:
#             if point[0] > batiment[0] and point[0] < batiment[1] and point[1] <= batiment[2]:
#                 h = batiment[2]
#
#         if is_valid(result, h):
#             result.append([point[0], h])
#
#     # solution = sorted(result)
#     # final_sol = []
#     #
#     # for point in solution:
#     #     if is_valid(final_sol, point[1]):
#     #         final_sol.append(point)
#
#     return result

#
# def brute(buildings: List[List[int]]):
#     result = []
#     for pos, point in enumerate(buildings):
#         left = [point[0], point[2]]
#         right = [point[0], 0]
#
#         for batiment in buildings[(pos+1):]:
#             print(batiment)
#             if left[0] > batiment[0] and left[0] < batiment[1] and left[1] <= batiment[2]:
#                 left[1] = batiment[2]
#             if right[0] > batiment[0] and right[0] < batiment[1]:
#                 right[1] = batiment[2]
#
#
#         if is_valid(result, left[1]):
#             result.append(left)
#         if is_valid(result, right[1]):
#             result.append(right)
#
#     solution = sorted(result)
#     final_sol = []
#
#     for point in solution:
#         if is_valid(final_sol, point[1]):
#             final_sol.append(point)
#
#     return final_sol
