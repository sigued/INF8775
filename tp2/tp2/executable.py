#!/usr/bin/env python3

import argparse
import numpy as np
import time
# import divide_and_conquer as dc
# import glouton as brute
# import dc_seuil as seuil
import glouton
import progdyn


def run(algo, path, print_time, print_couple):
    cities = np.loadtxt(path, dtype=int, skiprows=1)
    # city = [tuple(c) for c in cities]
    cities_index = list(range(len(cities)))

    if algo == 'glouton':
        begin = time.time()
        n, coord, D = glouton.read_cities(cities)
        tour = glouton.nearest_neighbor(n, 0, D)  # create a greedy tour, visiting city 'i' first
        end = time.time()

    if algo == 'progdyn':
        begin = time.time()
        progdyn.cost_matrix = progdyn.build_cost_matrix(cities)
        print(progdyn.cost_matrix)
        dist = progdyn.dynamic_TSP(0, 0, [1, 2, 3, 4])
        end = time.time()

    # if algo == 'seuil':
    #     begin = time.time()
    #     solution = seuil.divide_and_conquer_seuil(list_building, 102)
    #     end = time.time()

    # if print_couple:
    #     n = len(tour)
    #     print(tour)
    #     for i in range(n):
    #         if i == 1 and tour[1] > tour[n-1]:
    #             print(tour[n-1])
    #         elif i == (n-1) and tour[1] > tour[n-1]:
    #             print(tour[1])
    #         else:
    #             print(tour[i])
    #     print(tour[0])

    if print_time:
        print((end - begin) * 1000)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algo", \
                        help="Représente le type d'algorithme", \
                        action='store', required=True, metavar='NOM_ALGO', type=str)
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
    run(args.algo, args.chemin, args.time, args.affichage)
