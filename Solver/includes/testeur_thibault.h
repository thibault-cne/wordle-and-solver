//
// Created by Thibault Cheneviere on 06/06/2022.
//

#ifndef SOLVER_TESTEUR_THIBAULT_H
#define SOLVER_TESTEUR_THIBAULT_H

#include <string.h>

#include "core_char.h"
#include "core.h"
#include "core_node.h"

typedef struct best_word_result {
    char *word;
    double avg_turn;
} best_word_result;

void calculate_wordle_template(char *_template, char *good_word, char *_try);
int *init_nb_turn_result(int size);
double calculate_average(int *nb_turn_result);
double calculate_average_with_specific_best_word(char *best_word_value);

#endif //SOLVER_TESTEUR_THIBAULT_H
