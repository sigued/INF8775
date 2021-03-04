import csv
import os


import numpy as np
from tp1 import divide_and_conquer as dc
from tp1 import brute as brute
from tp1 import dc_seuil as seuil

donnees = "donnees"
result_file = 'time_result.csv'

with open(result_file, 'w', newline='') as csvFile:
    fw = csv.writer(csvFile, delimiter=',')
    fw.writerow(['Exemplaire', 'Taille exemplaire', 'Naif', 'Diviser pour regner', 'seuil'])
    for n in os.listdir(donnees):
        print(n)
        if str(n) == "1000" or str(n) == "10000" or str(n) == "100000" or str(n) == "5000" or str(n) == "50000" or str(n) == "500000":
            path = os.path.join(donnees, str(n))
            for file in os.listdir(path):
                print(file)
                file_path = os.path.join(path, file)

                my_buildings = np.loadtxt("./" + file_path, dtype=int, skiprows=1)
                buildings = my_buildings.tolist()

                time_naif = brute.time_execution_naif(buildings)
                time_dc = dc.time_execution_dv(buildings)
                time_seuil = seuil.time_execution_seuil(buildings, 256)
                fw.writerow([file, n, time_naif, time_dc, time_seuil])
