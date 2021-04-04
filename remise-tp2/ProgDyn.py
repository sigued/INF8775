# la logique de l'algorithme dynamaque dans la methode tsp_dynamic et get_minimum est tire du projet suivant:
# https://github.com/phvargas/TSP-python/blob/master/TSP.py

import math
import copy
import numpy as np


class Progdyn:
    def __init__(self, source, data, cities):
        self.data = data
        self.to_visit = range(1, len(cities))
        # self.to_visit = (1, 2, 3)
        self.n = len(data)
        self.matrix = self.build_cost_matrix(cities)
        # self.matrix = [[0, 10, 15, 20],
        #                [10, 0, 35, 25],
        #                [15, 35, 0, 30],
        #                [20, 25, 30, 0]]
        self.all_sets = []
        self.g = {}
        self.p = []
        self.source = source
        self.path = [source]

    def tsp_dynamic(self):
        for x in range(self.n):
            self.g[x, ()] = self.matrix[x][0]

        self.get_minimum(self.source, self.to_visit)

        solution = self.p.pop()
        self.path.append(solution[1][0])
        for x in range(self.n - 2):
            for new_solution in self.p:
                if tuple(solution[1]) == new_solution[0]:
                    solution = new_solution
                    self.path.append(solution[1][0])
                    break
        self.path.append(self.source)
        # print(g.popitem()[1])
        return self.path, self.g.popitem()[1]

    def get_minimum(self, k, a):
        if (k, a) in self.g:
            # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
            return self.g[k, a]

        values = []
        all_min = []
        for j in a:
            set_a = copy.deepcopy(list(a))
            set_a.remove(j)
            all_min.append([j, tuple(set_a)])
            result = self.get_minimum(j, tuple(set_a))
            values.append(self.matrix[k - self.source][j - self.source] + result)

        # get minimun value from set as optimal solution for
        self.g[k, a] = min(values)
        self.p.append(((k, a), all_min[values.index(self.g[k, a])]))

        return self.g[k, a]

    def dist(self, x1, y1, x2, y2):
        xdiff = (x2 - x1)
        ydiff = (y2 - y1)
        return round(math.sqrt(xdiff * xdiff + ydiff * ydiff))

    def build_cost_matrix(self, cities):
        n = len(cities)
        D = np.zeros((n, n)).astype(int)
        for i in range(n - 1):
            for j in range(i, n):
                if i == j:
                    D[i, j] = 0
                (x1, y1) = cities[i]
                (x2, y2) = cities[j]
                D[i, j] = self.dist(int(x1), int(y1), int(x2), int(y2))
                D[j, i] = D[i, j]
        return D

# def main(matrix):
#     for x in range(1, n):
#         g[x + 1, ()] = matrix[x][0]
#
#     get_minimum(source, cities)
#
#     # print('\n\nSolution to TSP: {1, ', end='')
#     path = [source]
#     solution = p.pop()
#     print(solution[1][0], end=', ')
#     for x in range(n - 2):
#         for new_solution in p:
#             if tuple(solution[1]) == new_solution[0]:
#                 solution = new_solution
#                 # print(solution[1][0], end=', ')
#                 path.append(solution[1][0])
#                 break
#     # print('1}')
#     return


# if __name__ == '__main__':
#     cities = np.loadtxt("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/DP_N15_0", dtype=int, skiprows=1)
#     cities_index = list(range(1, len(cities)))
#
#     # matrix = build_cost_matrix(cities)
#     # print(matrix)
#     # matrix = [
#     #     [0, 10, 15, 20],
#     #     [10, 0, 35, 25],
#     #     [15, 35, 0, 30],
#     #     [20, 25, 30, 0]]
#     main()
