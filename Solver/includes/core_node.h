//
// Created by Thibault Cheneviere on 30/05/2022.
//

#ifndef SOLVER_CORE_NODE_H
#define SOLVER_CORE_NODE_H


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "char_node.h"
#include "template_list.h"
#include "core_score.h"

typedef struct _best_word {
    char *word;
    double score;
} best_word;


// Functions to calculate the score of a word
void calculate_best_word(char_node *dictionary, int size, linked_list_template *template_list, best_word *best);
void calculate_best_word_recursive(char_node *root, char_node *dictionary, best_word *best, char *path, int depth, linked_list_template *template_list);

// Cut functions
void cut_words_for_calculation(char_node *root, char *user_response, char *word);
void cut_words_for_calculation_recursive(int depth, int template_temper, char word_temper, char_node *dictionary, int allowed_letters);
void cut_char_node(char_node *root, char *user_response, char *word);
void cut_char_node_recursive(int depth, int template_temper, char word_temper, char_node *dictionary, int allowed_letters);
bool check_letter_with_position_one(char *word, char *_template, char letter);

void init_dictionary_tree(FILE *file, char_node *dictionary, int MAX_WORD_SIZE);

best_word *init_best_word(char *word);
void copy_best_word(best_word *dest, best_word *src);
void free_best_word(best_word *best_word);

#endif //SOLVER_CORE_NODE_H
