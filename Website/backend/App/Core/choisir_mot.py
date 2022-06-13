from random import randint


from .coreFiles import open_txt


# fonction qui choisit le mot qui sera à deviner
def choisir_mot(tailleMot: int) -> str:
    # prend en entrée un chiffre et ouvre un .txt ou  tous les mots 
    # français de cette longueur (ou de la langue désirée) sont sur une ligne
    dico = open_txt("l_" + str(tailleMot)+"_reponse")
    longueur = len(dico)
    pos_mot = randint(1, longueur)
    mot = dico[pos_mot - 1][:-1]
    return mot
