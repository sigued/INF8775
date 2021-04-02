# import time
#
# import glouton
#
# def append_new_point(solution, x_coord, h_curr):
#     solution_size = len(solution)
#
#     if solution_size == 0:
#         solution.append([x_coord, h_curr])
#     else:
#         if solution[solution_size - 1][1] != h_curr:
#             solution.append([x_coord, h_curr])
#
#
# def merge_buildings(left, right):
#     total_left = len(left)
#     total_right = len(right)
#     h1 = h2 = 0
#     i = 0
#     j = 0
#     solution = []
#
#     while i < total_left and j < total_right:
#
#         if left[i][0] < right[j][0]:
#             point, h1 = left[i]
#             i += 1
#
#         else:
#             point, h2 = right[j]
#             j += 1
#
#         h_curr = max(h1, h2)
#         append_new_point(solution, point, h_curr)
#
#     solution.extend(left[i:])
#     solution.extend(right[j:])
#     return solution
#
#
# def divide_and_conquer_seuil(buildings, seuil):
#     n = len(buildings)
#
#     if n <= seuil:
#         return glouton.brute_algo(buildings)
#
#     if n == 0:
#         return []
#     if n == 1:
#         l, r, h = buildings[0]
#         return [[l, h], [r, 0]]
#
#     left_buildings = divide_and_conquer_seuil(buildings[: n // 2], seuil)
#     right_buildings = divide_and_conquer_seuil(buildings[n // 2:], seuil)
#     return merge_buildings(left_buildings, right_buildings)
#
#
# def time_execution_seuil(buildings, seuil):
#     start = time.time()
#     divide_and_conquer_seuil(buildings, seuil)
#     end = time.time()
#     return (end - start) * 1000
#
