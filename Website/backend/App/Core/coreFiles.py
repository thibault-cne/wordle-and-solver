#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : coreFiles.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4

# Import needed packages
import json
from pathlib import Path
from typing import List



def get_path(i: int) -> str:
    """
    A function to get the path of a file
    :param i: the number of parents you want to go back in the path
    :return: the needed path
    """
    cwd = Path(__file__).parents[i]
    cwd = str(cwd)
    return cwd


def read_json(filename: str) -> dict:
    """
    A function to read a json file
    :param filename: the json fileName
    :return: the content of the json file
    """
    cwd = get_path(2)
    
    with open(cwd+'/Data/Json/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data: dict, filename: str) -> None:
    """
    A function to write a json file
    :param data: the content of the dict you want to write
    :param filename: the file where you want to write
    """
    cwd = get_path(2)

    with open(cwd+'/Data/Json/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)


def open_txt(filename: str) -> List[str]:
    """
    A function to open a txt file and return a list of lines
    :param filename: the txt file you want to read
    :return: the list of all lines in the file
    """
    cwd = get_path(2)
    filePath = cwd + "/Data/Text/" + filename + ".txt"

    with open(filePath, 'r') as file:
        data = file.readlines()

    return data


def write_file(filename: str, filetype: str, folder: str, data: List[str]) -> None:
    cwd = get_path(2)
    cwd += '/Data/' + folder + '/' + filename + '.' + filetype

    with open(cwd, 'w') as file:
        for word in data:
            if word != "\n":
                file.write(word)

    return
