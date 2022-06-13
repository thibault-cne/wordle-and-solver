#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : louiscleriot
#   File : extractdico.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 4/28/22, 8:51 AM
import pandas as pd
import unidecode

df = pd.read_excel('../../Data/Lexique383.xlsb', engine='pyxlsb')
maxlettre = df["15_nblettres"].max()
"""
for taille in range(1, maxlettre + 1):
    liste = []
    for mot in df.loc[:, "3_lemme"]:
        if len(str(mot)) == taille:
            newmot = unidecode.unidecode(str(mot)) + "\n"
            if newmot not in liste:
                liste.append(newmot)
    with open("../../Data/Text/l_" + str(taille) + ".txt", "w") as f:
        for word in liste:
            if " " not in word and "-" not in word and "'" not in word:
                f.write(word)
df = df.sort_values(by='8_freqlemlivres', ascending=False)
df = df[df["8_freqlemlivres"] > 1.88]
for taille in range(1, maxlettre + 1):
    liste = []
    for mot in df.loc[:, "3_lemme"]:
        if len(str(mot)) == taille:
            newmot = unidecode.unidecode(str(mot)) + "\n"
            if newmot not in liste:
                liste.append(newmot)
    with open("../../Data/Text/l_" + str(taille) + "_reponse.txt", "w") as f:
        for word in liste:
            if " " not in word and "-" not in word and "'" not in word:
                f.write(word)
"""
for taille in range(1, maxlettre + 1):
    with open("../../Data/Text/l_" + str(taille) + "_reponse.txt", "r") as f:
        a = f.readlines()
    with open("../../Data/Text/dictionnary_reponse.txt", "a") as f:
        for li in a:
            f.write(li)
