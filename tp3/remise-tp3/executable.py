#!/usr/bin/env python3

import argparse
import numpy as np
import algo


def run(path, print_time, print_couple):
    matrix_dimensions = np.loadtxt(path, dtype=int, max_rows=1)
    n = matrix_dimensions[0]
    m = matrix_dimensions[1]
    matrix = np.loadtxt(path, dtype=int, skiprows=1)
    value = matrix[:n]
    cost = matrix[n:]
    value = value.tolist()
    cost = cost.tolist()

    bloc_value_matrix = np.subtract(value, cost)
    bloc_value_matrix = bloc_value_matrix.tolist()

    # test avec exemple de l'enonce
    # bloc_value_matrix = [[-1, 47, 81, -3, 21, 15],
    #         [0, 0, 0, 0, -30, -1],
    #         [-3, 321, -1, 53, -1, 0],
    #         [0, 537, -3, -3, 2, -1],
    #         [-5, 0, 0, 40, 320, 0],
    #         [-2, -2, 28, 450, -5, -5]]

    run_algo = algo.Progdyn()
    res, profit, index_res = run_algo.gold_profit_dyn_prog(bloc_value_matrix, n, m)
    run_algo.print_opt(index_res)


    # if print_couple:
    #     for s in solution:
    #         print(*s)

    # if print_time:
    #     print((end - begin) * 1000)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--chemin", \
                        help="Représente le chemin de l'exemplaires d'une même taille à tester", \
                        action='store', required=True, metavar='CH_EXEMPLAIRES', type=str)
    parser.add_argument("-p", "--affichage", \
                        help="affiche, sur chaque ligne, les couples définissant la silhouette de bâtiments", \
                        action='store_true')
    parser.add_argument("-t", "--time", \
                        help="Représente le temps d'execution de l'algorithme", \
                        action='store_true')

    args = parser.parse_args()
    run(args.chemin, args.time, args.affichage)
