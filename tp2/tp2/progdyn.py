#!/usr/bin/env python3
import math
import time

import numpy as np


def time_execution_dv(buildings):
    start = time.time()
    # divide_and_conquer(buildings)
    end = time.time()
    return (end - start) * 1000


def build_cost_matrix(cities):
    n = len(cities)
    D = {}  # dictionary to hold n times n matrix
    for i in range(n - 1):
        for j in range(i, n):
            if i == j:
                D[(i, j)] = 0
            (x1, y1) = cities[i]
            (x2, y2) = cities[j]
            D[i, j] = dist(x1, y1, x2, y2)
            D[j, i] = D[i, j]
    return D


def dist(x1, y1, x2, y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    return int(math.sqrt(xdiff * xdiff + ydiff * ydiff) + .5)


cost_matrix = {}


def GetCostVal(row, col, source):
    if col == 0:
        col = source
        return cost_matrix[(row, col)]
    return cost_matrix[(row, col)]


iterative_process = []
iterative_tour = []


def dynamic_TSP(main_source, source, cities):

    if len(cities) == 1:
        min_Dis = GetCostVal(source, cities[0], main_source) + GetCostVal(cities[0], 0, main_source)
        return min_Dis
    else:
        Dist = []
        tour = []
        for city in cities:
            d_cities = cities[:]
            d_cities.remove(city)
            tour.append(city)
            Dist.append(GetCostVal(source, city, source) + dynamic_TSP(main_source, city, d_cities))
        iterative_process.append(Dist)
        iterative_tour.append(tour)
        return min(Dist)

def tsp_best_tour(cities):
    best_tour = []
    c = 0
    best_tour.append(c)
    cs = [(range(1, len(cities)))]
    while True:
        l = dynamic_TSP(c, c, cs)
        lc = iterative_tour[(l.index(min(l)))]
        if lc == 0:
            break
        best_tour.append(lc)
        c = lc
        cs = cs.remove(lc)
    best_tour.append(0)
    # best_tour = tuple(reversed(best_tour))

    return best_tour

if __name__ == '__main__':
    cities = np.loadtxt("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/DP_N15_0", dtype=int, skiprows=1)
    cities_index = list(range(1, len(cities)))

    cost_matrix = build_cost_matrix(cities)
    # print(cost_matrix)
    dist = dynamic_TSP(0, 0, cities_index)
    print("------------------------------------>distance")
    print(min(iterative_process[-1]))
    # print("------------------------------------> tour")
    # # tour = tsp_best_tour(cities_index)
    # print(iterative_tour)


# def dynamic_TSP(main_source, source, cities):
#     if len(cities) == 1:
#         minDis = GetCostVal(source, cities[0], main_source) + GetCostVal(cities[0], 0, main_source)
#         return minDis
#     else:
#         Dist = []
#         for city in cities:
#             dcities = cities[:]
#             dcities.remove(city)
#             # print(city)
#             # print(cities)
#             # print(GetCostVal(source, city, source))
#             Dist.append(GetCostVal(source, city, source) + dynamic_TSP(main_source, city, dcities))
#         iterative_process.append(Dist)
#         return min(Dist)
