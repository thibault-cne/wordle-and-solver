import math

from .verif_motTI import verif_motTI
from ..Core.GenerateEveryTI import generatealltemplates


def wordle_ti(essai: str, possibility):
    # on enregistre la liste des mots disponibles dans possibility et le nombre des mots dans taille_avant
    taille_avant = len(possibility)
    # une fonction ecrite precedement genere toute les reponses possibles du positionnement des lettres du mot
    templates = generatealltemplates(len(essai))
    # initialisation des variables
    reponse = {}
    id = []
    bits = []
    essai = essai.lower()

    # on calcul pour chaque possibilité de placement de lettre le nombre de mot restant dans la liste
    for template in templates:
        tempPossiblity = possibility.copy()
        tempstr = ""
        for i in range(len(template)):
            tempstr += str(template[i])
        for mot in possibility:
            if verif_motTI(mot, essai) != tempstr and mot in tempPossiblity:
                tempPossiblity.remove(mot)
        # calcul de la proba du mot
        px = len(tempPossiblity) / taille_avant
        if px > 0:
            # calcul du Bits d'information associé
            information = -math.log(px, 2)
            # on rempli un dictionnaire avec la liste de mot obtenu, sa longueur, et le taux d'information obtenu
            dico = {
                "Bits": information,
                "NouvelleListe": tempPossiblity,
                "Longueur": len(tempPossiblity)
            }
            # on rempli le dictionnaire comportant tout les templates avec associé le dictionnaire précédent
            templateName = ""
            for i in template:
                templateName += str(i)
            reponse[templateName] = dico
    for t_id, t_info in reponse.items():
        id.append(t_id)
        bits.append(t_info["Bits"])
    return {"id": id[bits.index(min(bits))], "liste": reponse[id[bits.index(min(bits))]]["NouvelleListe"]}
