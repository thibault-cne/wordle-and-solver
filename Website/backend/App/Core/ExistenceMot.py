#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : louiscleriot
#  File : ExistenceMot.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/12
from os.path import abspath

from .coreFiles import open_txt


def ExistenceMot(mot: str) -> bool:
    data = open_txt("l_" + str(len(mot)))
    if mot + "\n" in data:
        return True
    else:
        return False
