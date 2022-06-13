# fonction qui verifie les mots et le nombre d'essais
# elle prend en le mot à deviner, le nb d'essais choisis par le joueur, l'essai en cours, et le n° de l'essai

def verif_motTI(solution: str, essai: str) -> dict:
    # on compte le nombre d'apparitions des lettres dans le mot de base
    compte = {}
    retour = ""
    for lettre in solution:
        compte[lettre] = 0
    for lettre in solution:
        compte[lettre] += 1

    # on crée un dico avec les positions des lettres essayées en clé et 0 en valeur par défaut
    dico = {}
    for i in range(len(essai)):
        dico[str(i)] = 0
    for i in range(len(essai)):
        if (essai[i] == solution[i]) and (compte[essai[i]] > 0):
            dico[str(i)] = 2
            compte[essai[i]] -= 1

    for i in range(len(essai)):
        if (essai[i] in solution) and (solution[i] != essai[i]) and (compte[essai[i]] > 0):
            dico[str(i)] = 1
            compte[essai[i]] -= 1

    for i in range(0, len(essai)):
        retour += str(dico[str(i)])
    return retour
