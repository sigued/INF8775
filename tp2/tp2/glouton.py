# https://stackoverflow.com/questions/30552656/python-traveling-salesman-greedy-algorithm

import math
import random
import time

import numpy as np


def distL2(x1, y1, x2, y2):
    """Compute the L2-norm (Euclidean) distance between two points.

    The distance is rounded to the closest integer, for compatibility
    with the TSPLIB convention.

    The two points are located on coordinates (x1,y1) and (x2,y2),
    sent as parameters"""
    xdiff = x2 - x1
    ydiff = y2 - y1
    return int(math.sqrt(xdiff * xdiff + ydiff * ydiff) + .5)




def mk_matrix(coord, dist):
    """Compute a distance matrix for a set of points.

    Uses function 'dist' to calculate distance between
    any two points.  Parameters:
    -coord -- list of tuples with coordinates of all points, [(x1,y1),...,(xn,yn)]
    -dist -- distance function
    """
    n = len(coord)
    D = np.zeros((n, n)).astype(int)  # dictionary to hold n times n matrix
    for i in range(n - 1):
        for j in range(i, n):
            if i == j:
                D[i, j] = 0
            (x1, y1) = coord[i]
            (x2, y2) = coord[j]
            D[i, j] = dist(int(x1), int(y1), int(x2), int(y2))
            D[j, i] = D[i, j]
    return n, D


def read_cities(cities):
    "basic function for reading a TSP problem on the TSPLIB format"
    "NOTE: only works for 2D euclidean or manhattan distances"

    dist = distL2

    xy_positions = cities

    n, D = mk_matrix(xy_positions, dist)
    return n, xy_positions, D


def mk_closest(D, n):
    """Compute a sorted list of the distances for each of the nodes.

    For each node, the entry is in the form [(d1,i1), (d2,i2), ...]
    where each tuple is a pair (distance,node).
    """
    C = []
    for i in range(n):
        dlist = [(D[i, j], j) for j in range(n) if j != i]
        dlist.sort()
        C.append(dlist)
    return C


def length(tour, D):
    """Calculate the length of a tour according to distance matrix 'D'."""
    z = D[tour[-1], tour[0]]  # edge from last to first city of the tour
    for i in range(1, len(tour)):
        z += D[tour[i], tour[i - 1]]  # add length of edge from city i-1 to i
    return z


def randtour(n):
    """Construct a random tour of size 'n'."""
    sol = range(n)  # set solution equal to [0,1,...,n-1]
    random.shuffle(sol)  # place it in a random order
    return sol


def nearest(last, unvisited, D):
    """Return the index of the node which is closest to 'last'."""
    near = unvisited[0]
    min_dist = D[last, near]
    for i in unvisited[1:]:
        if D[last, i] < min_dist:
            near = i
            min_dist = D[last, near]
    return near, min_dist


def nearest_neighbor(n, i, D):
    """Return tour starting from city 'i', using the Nearest Neighbor.

    Uses the Nearest Neighbor heuristic to construct a solution:
    - start visiting city i
    - while there are unvisited cities, follow to the closest one
    - return to city i
    """
    unvisited = list(range(n))
    unvisited.remove(i)
    last = i
    tour = [i]
    distance = []
    # print(D)
    while unvisited != []:
        next, dist = nearest(last, unvisited, D)
        tour.append(next)
        distance.append(dist)
        unvisited.remove(next)
        last = next
    tour.append(i)
    distance_to_first = D[last, i]
    distance.append(distance_to_first)
    return tour, np.sum(distance)


def time_glouton(cities):
    begin = time.time()
    n, coord, D = read_cities(cities)
    tour, dist = nearest_neighbor(n, 0, D)  # create a greedy tour, visiting city 'i' first
    end = time.time()
    return (end - begin) * 1000

#
#
#
# if __name__ == "__main__":
#     """Local search for the Travelling Saleman Problem: sample usage."""
#
#     #
#     # test the functions:
#     #
#
#     # random.seed(1)    # uncomment for having always the same behavior
#     import sys
#
#     if len(sys.argv) == 1:
#         # create a graph with several cities' coordinates
#         coord = [(4, 0), (5, 6), (8, 3), (4, 4), (4, 1), (4, 10), (4, 7), (6, 8), (8, 1)]
#         n, D = mk_matrix(coord, distL2)  # create the distance matrix
#         instance = "toy problem"
#     else:
#         instance = sys.argv[1]
#         n, coord, D = read_cities(instance)  # create the distance matrix
#         # n, coord, D = read_tsplib('INSTANCES/TSP/eil51.tsp')  # create the distance matrix
#
#     # function for printing best found solution when it is found
#     from time import clock
#
#     init = clock()
#
#
#     def report_sol(obj, s=""):
#         print
#         "cpu:%g\tobj:%g\ttour:%s" % \
#         (clock(), obj, s)
#
#
#     print
#     "*** travelling salesman problem ***"
#     print
#
#     # greedy construction
#     print
#     "greedy construction with nearest neighbor + local search:"
#     for i in range(n):
#         tour = nearest_neighbor(n, i, D)  # create a greedy tour, visiting city 'i' first
#         z = length(tour, D)
#         print
#         "nneigh:", tour, z, '  -->  ',
#     print
#
