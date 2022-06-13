from itertools import combinations_with_replacement, permutations


def generatealltemplates(longueur: int):
    valeurpossible = [0, 1, 2]
    sorties = list(combinations_with_replacement(valeurpossible, longueur))
    bruh = []
    listefinal=[]
    for sortie in sorties:
        bruh.append(list(set(permutations(sortie))))
    for bru in bruh :
        for br in bru :
            listefinal.append(br)
    return list(set(listefinal))
