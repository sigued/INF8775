import math

import numpy as np


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


def rec_tsp_solve(c, ts):
    assert c not in ts
    if ts:
        return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                   for lc in ts)
    else:
        return (d[0][c], 0)


def tsp_rec_solve(d):
    def rec_tsp_solve(c, ts):
        assert c not in ts
        if ts:
            my_set = min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc) for lc in ts)
            return my_set
        else:
            return (d[0][c], 0)

    best_tour = []
    c = 0
    best_tour.append(c)
    cs = set(range(1, len(d)))
    while True:
        l, lc = rec_tsp_solve(c, cs)
        if lc == 0:
            break
        best_tour.append(lc)
        c = lc
        cs = cs - set([lc])
    best_tour.append(0)
    # best_tour = tuple(reversed(best_tour))

    return best_tour


if __name__ == '__main__':
    cities = np.loadtxt("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/hard_N52", dtype=int, skiprows=1)

    # d = [
    #     [0, 10, 15, 20],
    #     [10, 0, 35, 25],
    #     [15, 35, 0, 30],
    #     [20, 25, 30, 0]]

    d = build_cost_matrix(cities)
    tour = tsp_rec_solve(d)
    c = 0
    cs = set(range(1, len(d)))
    l, lc = rec_tsp_solve(c, cs)
    print("------------------------------------>distance")
    print(l)
    print("------------------------------------>tour")
    print(tour)