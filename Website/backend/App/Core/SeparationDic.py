#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : louiscleriot
#  File : SeparationDic.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4
with open("../../../Data/Text/dictionnary.txt", "r") as fichier:
	tab=fichier.readlines()
taille={}
for i in range(1,27):
	liste = []
	for word in tab:
		word=word[:-1]
		if len(word) == i:
			liste.append(word)
	with open('../../../Data/Text/l_' + str(i) + '.txt',"w+") as file:
		for w in liste:
			file.write(w + '\n')