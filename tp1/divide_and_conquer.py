import argparse
import numpy as np
import time


# partie de code de l'algorithme divide_and_conquer inspire de https://www.learnbay.io/the-skyline-problem/
# partie de code de merge inspire de

def is_valid(self, result, new_height):
    return not result or result[-1][1] != new_height


def append_point(solution, curr_point, h_curr):
    if not solution:
        solution.append([curr_point, h_curr])
    else:
        if solution[-1][1] != h_curr:
            solution.append([curr_point, h_curr])


def append_new_point(solution, x_coord, h_curr):
    solution_size = len(solution)

    if solution_size == 0:
        solution.append([x_coord, h_curr])
    else:
        if solution[solution_size - 1][1] != h_curr:
            solution.append([x_coord, h_curr])


def merge_buildings(left, right):
    total_left = len(left)
    total_right = len(right)
    h1 = h2 = 0
    i = 0
    j = 0
    solution = []

    while i < total_left and j < total_right:

        if left[i][0] < right[j][0]:
            point, h1 = left[i]
            i += 1

        else:
            point, h2 = right[j]
            j += 1

        h_curr = max(h1, h2)
        append_new_point(solution, point, h_curr)

    solution.extend(left[i:])
    solution.extend(right[j:])
    return solution


def divide_and_conquer(buildings):
    n = len(buildings)

    if n == 0:
        return []
    if n == 1:
        l, r, h = buildings[0]
        return [[l, h], [r, 0]]

    left_buildings = divide_and_conquer(buildings[: n // 2])
    right_buildings = divide_and_conquer(buildings[n // 2:])
    return merge_buildings(left_buildings, right_buildings)


def run(algo, path, print_time):
    # 'C:/Users/Sid Ali/PycharmProjects/INF8775/tp1/N1000_0'
    my_buildings = np.loadtxt(path, dtype=int, skiprows=1)
    list_building = my_buildings.tolist()
    # print(list_building)

    if algo == 'recursif':
        begin = time.time()
        solution = divide_and_conquer(list_building)
        end = time.time()

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
    parser.add_argument("-t", "--time", \
                        help="Représente le temps d'execution de l'algorithme", \
                        action='store_true')

    args = parser.parse_args()
    run(args.algo, args.chemin, args.time)
