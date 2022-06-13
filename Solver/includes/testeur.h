// Copyright (c)
// Project : project2-E19
//
// --
//
// Author : louiscleriot
// File : testeur.h
// Description : *Enter description here*
//
// --
//
// Last modification : 2022/6/5

//
// Created by louiscleriot on 05/06/2022.
//

#ifndef PROJECT2_E19_TESTEUR_H
#define PROJECT2_E19_TESTEUR_H

#include "../includes/core.h"
#include "../includes/core_node.h"
#include <stdio.h>
#include <stdlib.h>

int hash_function(char c);
void wordle(char *_template, char *try,char *sol);
char *choose_word(int word_length,int current_line, int total_lines);
int get_number_of_line(FILE *file, int MAX_WORD_SIZE);




#endif //PROJECT2_E19_TESTEUR_H
