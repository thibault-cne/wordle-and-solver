import math
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
    compte = {}
    positions = {}
    valide = False
    lettrendouble = []
    # determination des lettres en double, de leur nombre et de leur position
    for lettre in essai:
        compte[lettre] = 0                       #initialisation du dict qui compte le nb d'apparition des lettres
        positions[lettre] = []                   #initialisation du dict qui save la position de chaque lettre
    for i in range(len(essai)):                  #i prend la valeure de chaque lettre du mot rentré par l'utilisateur
        lettre = essai[i]                        #lettre devient la ieme lettre du mot rentré par l'utilisateur
        compte[lettre] += 1                      #incremation du nb de l'apparition de la lettre dans le mot
        if compte[lettre] > 1:                   #si une lettre apparait plusieurs fois alors
            if lettre not in lettrendouble:      #on verifi que la lettre n'est pas deja dans les lettre du mot en double
                lettrendouble.append(lettre)     #on ajoute la lettre a la liste des lettre du mot en double
            valide = True                        #valide confirme la présence de lettre en plusieurs exmplaire
        positions[lettre].append(i)              #on ajoute la position de la lettre a la liste dans le dict
    # suppresion des templates impossibles
    if valide == True:                                                      #si des lettres en double sont présente
        for template in templates:
            tempSupr = False                                                #initialisation de la confirmation de la supp d'un template
            for let in lettrendouble:                                       #on parcour les lettre en double du mot rentré
                liste = []                                                  #initialisation de la liste des bits des lettre en double
                for pos in range(compte[let]):                              #compte[let] donne le nb d'apparition de la lettre
                    if template[positions[let][pos]] != 2:                  #si la valeur du bit de template de la lettre en double est duff de 2
                        liste.append(template[positions[let][pos]])         #on ajoute le bit dans la liste des bits des lettre en double
                for i in range(len(liste)-1):                                 #on parcours la liste des bits
                    S = liste[i] - liste[i + 1]                             #on calcul la différence entre 2 bits consecutif
                    if S == -1:                                             #si elle est négative (enchainement d'un zero puis d'un 1)
                        tempSupr = True                                     #on active la validation de la suppresion du template
            if tempSupr:
                templates.remove(template)                                  #suppresion du template
    # on calcul pour chaque possibilité de placement de lettre le nombre de mot restant dans la liste
    for template in templates:
        # on fait une liste des lettres qui doivent etre présente plusieurs fois dans les mots sauvegardé
        if valide:                                                                          #si le mot rentré a des lettre multiple
            comp2 = {}
            multlettre = []
            for letter in essai:                                                            #on parcours les lettres du mot rentré
                comp2[letter] = 0
            for letter in range(len(essai) - 1):
                if template[letter] == 1 or template[letter] == 2:                          #si le bits =1 ou 2 on ajoute sa présence dans un dict
                    comp2[essai[letter]] += 1
                    if comp2[essai[letter]] > 1 and essai[letter] not in multlettre:        #si une lettre est validé plusieurs fois et pas encore présente
                        multlettre.append(essai[letter])                                    #dans la liste, on l'ajoute a liste des lettres multiple
        #initialisation de la liste qur l'on va reduir
        tempPossiblity = possibility.copy()
        #on parcours cette liste
        for mot in possibility:
            # On applique le template
            for j in range(len(template)):
                step = template[j]
                # si la lettre n'y est pas
                if step == 0:
                    # on regarde dans la grosse liste l_taille.txt
                    # si la jeme lettre du mot n,est pas dans un des mots de la liste on l'ajoute a la liste des possibilité
                    if essai[j] in mot and mot in tempPossiblity:
                        tempPossiblity.remove(mot)
                # si la lettre est mal placé
                elif step == 1:
                    if essai[j] not in mot and mot in tempPossiblity:
                        tempPossiblity.remove(mot)
                    if essai[j] == mot[j] and mot in tempPossiblity:
                        tempPossiblity.remove(mot)

                # si la lettre est a la bonne place
                elif step == 2:
                    if essai[j] != mot[j] and mot in tempPossiblity:
                        tempPossiblity.remove(mot)
            #on supprime les mots restant ne contenant pas le bon nombre de lettre
            if valide:
                comp3 = {}
                for letretest in mot:                                 #pour chaque lettre du mot de la liste
                    comp3[letretest] = 0                            #initiliser le nb d'occurence a 0
                for letretest in mot:
                    comp3[letretest] += 1                           #augmenter le compteur d'apparition
                for k in range(len(multlettre)):                    #on parcours les lettres en double validé du mot rentré
                    if multlettre[k] in mot:                          #si cette lettre est dans le mot
                        if comp3[multlettre[k]] < comp2[multlettre[k]] and mot in tempPossiblity: #et qu'elle a moins d'occurence que dans ce qui
                            tempPossiblity.remove(mot)                                            #prevu par le template on enleve le mot
                    elif mot in tempPossiblity:
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
