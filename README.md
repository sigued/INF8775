# INF8775
Analyse et conception d'algorithmes

-Pour trouver le seuil de r�cursivitéideal entre un algorithme diviser pour regner et de force brute (r�sultat dans dossier seuil_dc), executer la commande:
python3 seuil.py

-pour afficher le temps d'ex�cution d'un jeu de donn�es ( voir fichier time_result.csv), ex�cuter la commande:
python3 timeToCsv.py

G�neration des donn�es:
$ ./inst_gen.py [-h] -s NB_BATIMENTS [-n NB_EXEMPLAIRES]

Visualition des r�sultat du skyline problem dans le dossier tp1:
$ ./tp.sh -a {brute, recursif, seuil} -e CHEMIN_EXEMPLAIRE [-p] [-t]
Arguments optionnels :
[-p] affiche, sur chaque ligne, les couples définissant la silhouette de bâtiments, triés selon l’abscisse et sans texte superflu (les deux valeurs d’un couple sont séparées d’un espace) ;
[-t] affiche le temps d’exécution en millisecondes, sans unité ni texte superflu.

