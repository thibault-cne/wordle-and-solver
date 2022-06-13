// Copyright (c)
// Project : project2-E19
//
// --
//
// Author : louiscleriot
// File : testeur.c
// Description : *Enter description here*
//
// --
//
// Last modification : 2022/6/5

//
// Created by louiscleriot on 05/06/2022.
//
#include "../includes/testeur_thibault.h"


int main(){
    char *n = word_length();
    int word_length = atoi(n);

    char **paths =get_all_path();
    FILE *file = open_txt(paths[word_length]);

    char *line = malloc(sizeof(char) * (word_length + 2));

    best_word_result *best_result_word = malloc(sizeof(best_word_result));
    best_result_word->avg_turn = -1;

    while(fgets(line, word_length + 2, file) != NULL) {
        line[word_length] = '\0';

        double avg_turn = calculate_average_with_specific_best_word(line);

        if (avg_turn > best_result_word->avg_turn) {
            best_result_word->avg_turn = avg_turn;
            best_result_word->word = strdup(line);
        }
    }

    printf("Best brute force word %s\n", best_result_word->word);

    return 0;
}


