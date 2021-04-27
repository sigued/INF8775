# la logique de l'algorithme dynamaque dans la methode tsp_dynamic et get_minimum est tire du projet suivant:
# https://github.com/phvargas/TSP-python/blob/master/TSP.py

import itertools
import math


class Progdyn:
    # def __init__(self, m):
    #     self.ind = [0, 1, 2, 3, 4, 5]
    #     if m < 10:
    #         self.combs = [self.ind for i in range(m)]
    #     else:
    #         self.combs = [self.ind for i in range(10)]
    #
    #     self.all_comb = list(itertools.product(*self.combs))
    #     self.index = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    def gold_profit_dyn_prog(self, gold, m, n):

        goldTable = [[0 for i in range(n)]
                     for j in range(m)]

        for row in range(n):
            for col in range(m):

                # La premiere du tableau est egale a la valeur de l'or a laquelle on soustrait le cout
                # la premiere ligne du tableau fait partie des valeurs frontières pour notre algorithme
                if (row == 0):
                    left = 0
                    mid = 0
                    right = 0
                # ensuite on verifie Si un de ces couples se trouve être en dehors des limites du tableau. Si c'est le cas, son bloc correspondant sera considéré comme déjà extrait.
                elif (col - 1 < 0 and row > 0):
                    left = 0
                    mid = goldTable[row - 1][0]
                    right = goldTable[row - 1][1]
                # on verifie toujours si un de ces couples se trouve être en dehors des limites du tableau.
                elif (col == m - 1 and row > 0):
                    left = goldTable[row - 1][col - 1]
                    mid = goldTable[row - 1][col]
                    right = 0
                else:
                    left = goldTable[row - 1][col - 1]
                    mid = goldTable[row - 1][col]
                    right = goldTable[row - 1][col + 1]

                # Enfin, sinon on remplie la case du i, j du tableau selon la relation de recurrence : matrice_de_profit[i][j] + max { blocs (i – 1, j – 1), (i – 1, j) et (i – 1, j + 1) }
                goldTable[row][col] = gold[row][col] + max(mid, left, right)

            # construction du path
            # --------------------------------------------------------------
            # on commence par determiner la valeur maximale trouvee dans le tableau de la valeur d'or acquise (goldTable) : rows = index de cette valeur max
            # Dans le cas ou la valeur max est se trouve a diffentes lignes tableau, on choisit la donnee calculee pour la premiere fois.
            rows, cols = (goldTable.index(max(goldTable, key=max)), 2)
            index_tab = [[0 for i in range(cols)] for j in range(rows + 1)]
            col_of_max = (goldTable[goldTable.index(max(goldTable, key=max))])
            index_tab[rows][0] = index_tab[rows][1] = col_of_max.index(max(col_of_max))

            # A partir du gain maximal, on reconstruit le parcours minimal effectue pour pouvoir se rendre a cette emplacement
            for i in range(rows - 1, -1, -1):
                if index_tab[i + 1][0] - 1 < 0:
                    index_tab[i][0] = 0
                else:
                    index_tab[i][0] = index_tab[i + 1][0] - 1

                if index_tab[i + 1][1] + 1 >= m - 1:
                    index_tab[i][1] = m - 1
                else:
                    index_tab[i][1] = index_tab[i + 1][1] + 1

        # on retourne le gain (rows), le tableau de profits et le table pour pouvoir reconstruire le chemin
        return rows, goldTable, index_tab

    # Fonction pour imprimer le parcours du robot
    def print_opt(self, index_tab):
        rows = len(index_tab)
        for i in range(rows):
            path = []
            blocs = (index_tab[i][1] - index_tab[i][0]) + 1

            for bloc in range(blocs):
                x, y = (i, index_tab[i][0] + bloc)
                print(str(x) + " " + str(y))
        print("\n", flush=True)



    # def print_path(self, index_tab):
    #     print(self.index)
    #     rows = len(index_tab)
    #     for comb in self.all_comb:
    #         for k in comb:
    #             for i in range(rows):
    #                 print(str(i) + "----------")
    #                 my_set = set()
    #                 blocs = math.ceil((index_tab[i][1] - index_tab[i][0]) / 3)
    #                 if  blocs == 0:
    #                     my_set.add((index_tab[i][0], index_tab[i][0]))
    #                 for bloc in range(blocs):
    #
    #                     for j in self.index[k]:
    #                         x, y = (i, index_tab[i][0] + bloc + j)
    #                         my_set.add((x, y))
    #                 print((my_set))
    #             print("\n", flush=True)


# if __name__ == '__main__':
#     gold = [[-1, 47, 81, -3, 21, 15],
#             [0, 0, 0, 0, -30, -1],
#             [-3, 321, -1, 53, -1, 0],
#             [0, 537, -3, -3, 2, -1],
#             [-5, 0, 0, 40, 320, 0],
#             [-2, -2, 28, 450, -5, -5]]
#
#     # gold = [[1, 3, 1, 5],
#     #         [2, 2, 4, 1],
#     #         [5, 0, 2, 3],
#     #         [0, 6, 1, 2]]
#
#     m = 6
#     n = 6
#
#     test = Progdyn()
#     res, goldTable, index_res = test.gold_profit_dyn_prog(gold, m, n)
#     test.print_opt(index_res)
#
#     # lst = [[-1, 47, 81, -3, 21, 15], [47, 81, 81, 81, -9, 22220], [78, 402, 80, 134, 80, 20], [402, 939, 399, 131, 136, 79], [934, 939, 939, 439, 456, 136], [937, 937, 967, 1389, 451, 451]]
#     # print(lst.index(max(lst, key=max)))
#     # print(res)
