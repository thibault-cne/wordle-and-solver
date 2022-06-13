//
// Created by Thibault Cheneviere on 27/05/2022.
//

#ifndef SOLVER_CORE_H
#define SOLVER_CORE_H

#include <string.h>
#include <stdbool.h>

#include "core_char.h"

char **get_all_path();
void free_all_path(char **paths);
FILE* open_txt(char* path);
char* word_length();
char *get_best_opening(int word_length);
bool check_template_validity(char *template);

#endif //SOLVER_CORE_H
