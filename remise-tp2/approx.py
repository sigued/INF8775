# code tire d'un projet similaire trouve sur github. apres analyse du code nous avons constate qu'il repondait au critere du present tp
# nous avons adapte la construction des noeuds aux fichiers de tests que nous avions, mais la logique est tire du projet suivant:
# https://github.com/sleepy-juan/Travelling-Salesman-Problem/tree/e6aca323854ccceb306093c4e49d25c4dc43e1e0/tsp
# Writtenn by Juan Lee (juanlee@kaist.ac.kr)

import time

import numpy as np

##################################################
# Node Utilities
#

# node structure
# id: {id, x, y}
def distanceBtw(f, t):
    return ((int(f['x']) - int(t['x'])) ** 2 + (int(f['y']) - int(t['y'])) ** 2) ** 0.5

# path structure
# [p1, p2, ..., pn]
def distance(path, nodes):
    dist = 0
    for idx in range(len(path)):
        cur = path[idx]
        nxt = path[(idx + 1) % len(path)]

        dist += distanceBtw(nodes[cur], nodes[nxt])
    return dist


def distanceOfEdges(nodes):
    dists = {}
    asList = []
    keys = list(nodes.keys())
    for i in range(len(keys)):
        ki = keys[i]
        dists[(ki, ki)] = 0
        for j in range(i + 1, len(keys)):
            kj = keys[j]
            d = distanceBtw(nodes[ki], nodes[kj])
            dists[(ki, kj)] = d
            dists[(kj, ki)] = d

            asList.append((ki, kj, d))
    return dists, asList


def saveDistance(filename, distanceTable, dimension):
    with open(filename, 'w') as f:
        for i in range(dimension):
            for j in range(dimension):
                f.write(str(distanceTable[(i + 1, j + 1)]) + ", ")
            f.write("\n")


def loadDistance(filename, dimension):
    distanceTable = {}
    with open(filename, 'r') as f:
        for i in range(dimension):
            line = f.readline().strip().split(",")
            distanceTable[(i, i)] = 0
            for j in range(i + 1, dimension):
                dist = float(line[j])
                distanceTable[(i + 1, j + 1)] = dist
                distanceTable[(j + 1, i + 1)] = dist
    return distanceTable


##################################################
# File Utilities
#

def build_nodes(filename):
    nodes = {}
    cities = np.loadtxt(filename, dtype=int, skiprows=1)
    parsed = [list(c) for c in cities]
    n = 0
    for c in (parsed):
        c.insert(0, n)
        n += 1
    parsed = [tuple(c) for c in parsed]

    for node in parsed:
        nodes[int(node[0])] = {
            "id": int(node[0]),
            "x": node[1],
            "y": node[2]
        }

    return nodes

##################################################
# TSP Utils
#

def spanning_tree(table, edges, nodes):
    edges.sort(key=lambda node: node[2])  # sort by distance
    vertice = [{
        "group": -1,
        "id": i,
        "neighbors": []
    } for i in range(len(nodes.keys()) + 1)]
    nEst = 0
    groupIdToAssign = 0

    # from the shortest
    for edge in edges:
        x, y, dist = edge

        vx = vertice[x]
        vy = vertice[y]

        # node is already connected
        if len(vx["neighbors"]) == 2 or len(vy["neighbors"]) == 2:
            continue
        # nodes are same group; it makes cycle
        if vx["group"] == vy["group"] and vx["group"] != -1:
            continue

        vx["neighbors"].append(y)
        vy["neighbors"].append(x)

        # group rearranging
        if vx["group"] == vy["group"]:  # only if group == -1
            vx["group"] = groupIdToAssign
            vy["group"] = groupIdToAssign
            groupIdToAssign += 1
        elif vx["group"] == -1:  # only vx is solo
            vx["group"] = vy["group"]
        elif vy["group"] == -1:
            vy["group"] = vx["group"]
        else:  # both nodes has own group
            xg = vx["group"]
            yg = vy["group"]
            for vertex in vertice:
                if vertex["group"] == yg:
                    vertex["group"] = xg

        nEst += 1
        if nEst == len(nodes.keys()):
            break

    single = []
    for vertex in vertice:
        if len(vertex["neighbors"]) < 2 and vertex["id"] != 0:
            single.append(vertex["id"])

    vertice[single[0]]["neighbors"].append(single[1])
    vertice[single[1]]["neighbors"].append(single[0])

    result = [0]
    while len(result) < len(nodes.keys()):
        current = result[-1]
        neighbors = vertice[current]["neighbors"]
        if neighbors[0] in result:
            result.append(neighbors[1])
        else:
            result.append(neighbors[0])
    result.append(0)
    return result


##################################################
# Main
#

argument = {}


def solve(nodes):
    table, edges = distanceOfEdges(nodes)
    # printIf("Distance Calculation Done", argument["-l"])
    return spanning_tree(table, edges, nodes)


def tsp_mst(tsp_file, args={"-l": True}):
    global argument
    argument = args

    nodes = build_nodes(tsp_file)

    begin = time.time()
    path = solve(nodes)
    end = time.time()
    time_mst = (end - begin) * 1000

    dist = distance(path, nodes)

    # print(dist)
    # print(time_mst)
    return time_mst, path, round(dist)


# if __name__ == '__main__':
#     tsp_mst("C:/Users/Sid Ali/PycharmProjects/INF8775-tp2/donnees/DP_N5/DP_N5_0")
