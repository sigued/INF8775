import math
import os
import random
from tp1 import dc_seuil as dc_seuil

import numpy as np


def find_limit(path):
    my_buildings = np.loadtxt(path, dtype=int, skiprows=1)
    buildings = my_buildings.tolist()

    nb_test_min = math.inf
    seuil = random.randint(10, 2000)
    temp = math.inf
    curr = math.inf

    while curr <= temp and nb_test_min > 1:
        nb_test_min = seuil
        seuil = max(int(nb_test_min / 2), 1)
        temp = curr
        curr = dc_seuil.time_execution_seuil(buildings, seuil)

    return nb_test_min


def getAverageNminForSampleSize(test_directory, n):
    i = 0
    sumNmin = 0
    path = os.path.join(test_directory, str(n))
    for file in os.listdir(path):
        sumNmin += find_limit(os.path.join(path, file))
        i += 1
    return int(sumNmin / i)


def getOverallAverageNmin(test_directory):
    i = 0
    sumNmin = 0
    fn = os.path.join("seuil_dc", "seuil_dc.txt")
    with open(fn, 'w') as f:
        for n in os.listdir(test_directory):
            nMin = getAverageNminForSampleSize(test_directory, n)
            print("seuil de recursivité: " + str(nMin) + ", sample size: " + str(n))
            f.write("seuil de recursivité: " + str(nMin) + ", sample size: " + str(n) + '\n')
            sumNmin += nMin
            i += 1
        f.write("seuil de recursivité moyenne: " + str(int(sumNmin / i)) + '\n')
    f.close()
    return int(sumNmin / i)


print(getOverallAverageNmin("donnees"))
