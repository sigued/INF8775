#!/usr/bin/env python3

import argparse
import numpy as np
import time

import glouton
from ProgDyn import Progdyn
import approx


def run(algo, path, print_time, print_couple):
    cities = np.loadtxt(path, dtype=int, skiprows=1)
    # city = [list(c) for c in cities]
    # n = 0
    # for c in (city):
    #     c.insert(0, n)
    #     n+=1
    # city = [tuple(c) for c in city]
    #
    # print(city)

    data = list(range(len(cities)))
    # print(data)
    # data = [1, 2, 3, 4]

    time_calculated = False

    if algo == 'glouton':
        n, coord, D = glouton.build_cost_matrix(cities)
        begin = time.time()
        tour, dist = glouton.tsp_greedy(n, 0, D)  # create a greedy tour, visiting city 'i' first
        end = time.time()
        time_calculated = True

    if algo == 'progdyn':
        progdyn = Progdyn(0, data, cities)
        begin = time.time()
        tour, dist = progdyn.tsp_dynamic()
        end = time.time()
        time_calculated = True

    if algo == 'approx':
        time_approx, tour, dist = approx.tsp_mst(path)

    if print_couple:
        print(tour)
        for city in tour:
            if city == tour[1] and tour[1] > tour[-2]:
                print(tour[-2])
            elif city == tour[-2] and tour[1] > tour[-2]:
                print(tour[1])
            else:
                print(city)
        # print(dist)
        # print((end - begin) * 1000)

    if print_time:
        if time_calculated:
            print((end - begin) * 1000)
        else:
            print(time_approx)


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
