import csv
import os
import time

import numpy as np

from tp2 import glouton
from tp2.ProgDyn import Progdyn

donnees = "donnees"
result_file = 'time_result.csv'

with open(result_file, 'w', newline='') as csvFile:
    fw = csv.writer(csvFile, delimiter=',')
    fw.writerow(['Exemplaire', 'Taille exemplaire', 'glouton', 'progdyn'])
    for n in os.listdir(donnees):
        print(n)
        if str(n) == "1000" or str(n) == "5000" or str(n) == "10000" or str(n) == "50000" or str(n) == "100000":
            path = os.path.join(donnees, str(n))
            for file in os.listdir(path):
                # print(file)
                file_path = os.path.join(path, file)
                print(file_path)

                cities = np.loadtxt("./" + file_path, dtype=int, skiprows=1)
                data = list(range(len(cities)))

                time_glouton = glouton.time_glouton(cities)

                fw.writerow([file, n, time_glouton])

        if str(n) == "DP_N5" or str(n) == "DP_N10" or str(n) == "DP_N15" or str(n) == "DP_N20" or str(n) == "DP_N25":
            path = os.path.join(donnees, str(n))
            for file in os.listdir(path):
                # print(file)
                file_path = os.path.join(path, file)
                print(file_path)

                cities = np.loadtxt("./" + file_path, dtype=int, skiprows=1)
                data = list(range(len(cities)))

                time_glouton = glouton.time_glouton(cities)

                begin = time.time()
                progdyn = Progdyn(0, data, cities)
                tour, dist = progdyn.main()
                end = time.time()

                time_progDyn = (end - begin) * 1000

                fw.writerow([file, n, time_glouton, time_progDyn])

