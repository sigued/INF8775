#!/usr/bin/env python3

import argparse
import numpy as np
import time
import divide_and_conquer as dc
import brute as brute
import dc_seuil as seuil


def run(algo, path, print_time, print_couple):
    # 'C:/Users/Sid Ali/PycharmProjects/INF8775/tp1/N1000_0'
    my_buildings = np.loadtxt(path, dtype=int, skiprows=1)
    list_building = my_buildings.tolist()
    # print(list_building)
    # list_building = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    if algo == 'brute':
        # pts_critic = brute.critic_pts(list_building)
        begin = time.time()
        solution = brute.getSkyline(list_building)
        end = time.time()

    if algo == 'recursif':
        begin = time.time()
        solution = dc.divide_and_conquer(list_building)
        end = time.time()

    if algo == 'seuil':
        begin = time.time()
        solution = seuil.divide_and_conquer_seuil(list_building, 102)
        end = time.time()

    if print_couple:
        for s in solution:
            print(*s)

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
