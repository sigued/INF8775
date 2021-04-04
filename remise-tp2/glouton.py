# code tiré d'une discussion stackoverflow et adapté au contexte du present tp. Le lien est le suivant:
# https://stackoverflow.com/questions/30552656/python-traveling-salesman-greedy-algorithm

import math
import time

import numpy as np


def dist(x1, y1, x2, y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    return round(math.sqrt(xdiff * xdiff + ydiff * ydiff))


def cost_matrix(coord):
    n = len(coord)
    D = [[0 for c in range(n)] for r in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            (x1, y1) = coord[i]
            (x2, y2) = coord[j]
            D[i][j] = dist(int(x1), int(y1), int(x2), int(y2))
            D[j][i] = D[i][j]
    return n, D


def build_cost_matrix(cities):
    xy_positions = cities
    n, D = cost_matrix(xy_positions)

    return n, xy_positions, D


def find_nearest(last, unvisited, D):
    near = unvisited[0]
    min_dist = D[last][near]
    for i in unvisited[1:]:
        if D[last][i] < min_dist:
            near = i
            min_dist = D[last][near]
    return near, min_dist


def tsp_greedy(n, i, D):
    unvisited = list(range(n))
    unvisited.remove(i)
    last = i
    tour = [i]
    distance = []
    # print(D)
    while unvisited != []:
        next, dist = find_nearest(last, unvisited, D)
        tour.append(next)
        distance.append(dist)
        unvisited.remove(next)
        last = next
    tour.append(i)
    distance_to_first = D[last][i]
    distance.append(distance_to_first)
    return tour, np.sum(distance)


def time_greedy(cities):
    n, coord, D = build_cost_matrix(cities)
    begin = time.time()
    tour, dist = tsp_greedy(n, 0, D)  # create a greedy tour, visiting city 'i' first
    end = time.time()
    return (end - begin) * 1000
