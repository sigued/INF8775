#!/usr/bin/env python3


import heapq
import time
from typing import List


def time_execution_naif(buildings):
    start = time.time()
    brute_algo(buildings)
    end = time.time()
    return (end - start) * 1000


def brute_algo(buildings: List[List[int]]):
    point_critic = []
    for building in buildings:
        point_critic.extend([[building[0], building[2]]])
        point_critic.extend([[building[1], 0]])
    point_critic.sort()
    result = []
    heapq.heapify(result)

    for point in point_critic:
        for batiment in buildings:
            if point[0] > batiment[0] and point[0] < batiment[1] and point[1] <= batiment[2]:
                h = batiment[2]
                point[1] = batiment[2]

        if not result or result[-1][1] != point[1]:
            heapq.heappush(result, point)

    return result
