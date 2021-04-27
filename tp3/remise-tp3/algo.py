import sys


class Progdyn:

    def gold_profit_dyn_prog(self, gold, n, m):

        profit = [[0 for i in range(m)]
                     for j in range(n)]

        for row in range(n):
            for col in range(m):

                # La premiere du tableau est egale a la valeur de l'or a laquelle on soustrait le cout
                # la premiere ligne du tableau fait partie des valeurs frontières pour notre algorithme
                if (row == 0):
                    left = 0
                    mid = 0
                    right = 0
                # ensuite on verifie Si un de ces couples se trouve être en dehors des limites du tableau. Si c'est le cas, son bloc correspondant sera considéré comme déjà extrait.
                elif (col - 1 < 0 and row > 0):
                    left = 0
                    mid = profit[row - 1][0]
                    right = profit[row - 1][1]
                # on verifie toujours si un de ces couples se trouve être en dehors des limites du tableau.
                elif (col == m - 1 and row > 0):
                    left = profit[row - 1][col - 1]
                    mid = profit[row - 1][col]
                    right = 0
                else:
                    left = profit[row - 1][col - 1]
                    mid = profit[row - 1][col]
                    right = profit[row - 1][col + 1]

                # Enfin, sinon on remplie la case du i, j du tableau selon la relation de recurrence : matrice_de_profit[i][j] + max { blocs (i – 1, j – 1), (i – 1, j) et (i – 1, j + 1) }
                profit[row][col] = gold[row][col] + max(mid, left, right)

        # construction du path
        # --------------------------------------------------------------
        # on commence par determiner la valeur maximale trouvee dans le tableau de la valeur d'or acquise (profit) : rows = index de cette valeur max
        # Dans le cas ou la valeur max est se trouve a diffentes lignes tableau, on choisit la donnee calculee pour la premiere fois.
        rows, cols = (profit.index(max(profit, key=max)), 2)
        index_tab = [[0 for i in range(cols)] for j in range(rows + 1)]
        col_of_max = (profit[profit.index(max(profit, key=max))])
        index_tab[rows][0] = index_tab[rows][1] = col_of_max.index(max(col_of_max))

        # A partir du gain maximal, on reconstruit le parcours minimal effectue pour pouvoir se rendre a cette emplacement
        for i in range(rows - 1, -1, -1):
            if index_tab[i + 1][0] - 1 < 0:
                index_tab[i][0] = 0
            else:
                index_tab[i][0] = index_tab[i + 1][0] - 1

            if index_tab[i + 1][1] + 1 >= m - 1:
                index_tab[i][1] = m - 1
            else:
                index_tab[i][1] = index_tab[i + 1][1] + 1

        # on retourne le gain (rows), le tableau de profits et le table pour pouvoir reconstruire le chemin
        return rows, profit, index_tab

    # Fonction pour imprimer le parcours du robot
    def print_opt(self, index_tab):
        rows = len(index_tab)
        for i in range(rows):
            path = []
            blocs = (index_tab[i][1] - index_tab[i][0]) + 1

            for bloc in range(blocs):
                x, y = (i, index_tab[i][0] + bloc)
                print(str(x) + " " + str(y))
        sys.stdout.flush()




