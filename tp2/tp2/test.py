# import math
#
# import numpy as np
#
#
# def dist(x1, y1, x2, y2):
#     xdiff = (x2 - x1)
#     ydiff = (y2 - y1)
#     return round(math.sqrt(xdiff * xdiff + ydiff * ydiff))
#
#
# def build_cost_matrix(cities):
#     n = len(cities)
#     D = np.zeros((n, n)).astype(int)  # dictionary to hold n times n matrix
#     for i in range(n - 1):
#         for j in range(i, n):
#             if i == j:
#                 D[i, j] = 0
#             (x1, y1) = cities[i]
#             (x2, y2) = cities[j]
#             D[i, j] = dist(int(x1), int(y1), int(x2), int(y2))
#             D[j, i] = D[i, j]
#     return D
#
#
# def rec_tsp_solve(c, ts):
#     assert c not in ts
#     if ts:
#         return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
#                    for lc in ts)
#     else:
#         return (d[0][c], 0)
#
#
# def tsp_rec_solve(d):
#     def rec_tsp_solve(c, ts):
#         assert c not in ts
#         if ts:
#             my_set = min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc) for lc in ts)
#             return my_set
#         else:
#             return (d[0][c], 0)
#
#     best_tour = []
#     c = 0
#     best_tour.append(c)
#     cs = set(range(1, len(d)))
#     while True:
#         l, lc = rec_tsp_solve(c, cs)
#         if lc == 0:
#             break
#         best_tour.append(lc)
#         c = lc
#         cs = cs - set([lc])
#     best_tour.append(0)
#     # best_tour = tuple(reversed(best_tour))
#
#     return best_tour
#
#
# if __name__ == '__main__':
#     cities = np.loadtxt("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/DP_N15_0", dtype=int, skiprows=1)
#
#     # d = [
#     #     [0, 10, 15, 20],
#     #     [10, 0, 35, 25],
#     #     [15, 35, 0, 30],
#     #     [20, 25, 30, 0]]
#
#     d = build_cost_matrix(cities)
#     # tour = tsp_rec_solve(d)
#     c = 0
#     cs = set(range(1, len(d)))
#     l, lc = rec_tsp_solve(c, cs)
#     print("------------------------------------>distance")
#     print(l)
#     print("------------------------------------>tour")
#     # print(tour)
import copy
import math

import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""
for test purposes
matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
data = [1, 2, 3, 4]
"""
n = len(data)
all_sets = []
g = {}
p = []


def dist(x1, y1, x2, y2):
    xdiff = (x2 - x1)
    ydiff = (y2 - y1)
    return round(math.sqrt(xdiff * xdiff + ydiff * ydiff))


def build_cost_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n)).astype(int)  # dictionary to hold n times n matrix
    for i in range(n - 1):
        for j in range(i, n):
            if i == j:
                D[i, j] = 0
            (x1, y1) = cities[i]
            (x2, y2) = cities[j]
            D[i, j] = dist(int(x1), int(y1), int(x2), int(y2))
            D[j, i] = D[i, j]
    return D


def main(matrix):
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    get_minimum(1, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k - 1][j - 1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    cities = np.loadtxt("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/DP_N20_0", dtype=int, skiprows=1)
    cities_index = list(range(1, len(cities)))

    matrix = build_cost_matrix(cities)
    # print(matrix)
    # matrix = [
    #     [0, 10, 15, 20],
    #     [10, 0, 35, 25],
    #     [15, 35, 0, 30],
    #     [20, 25, 30, 0]]
    main(matrix)
