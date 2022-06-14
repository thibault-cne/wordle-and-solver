//
// Created by Thibault Cheneviere on 06/06/2022.
//

#include "../includes/testeur.h"


void calculate_wordle_template(char *template, char *good_word, char *try) {
    int i = 0;
    int *char_number = _count_all_char(good_word);

    while (good_word[i] != '\0') {
        if (try[i] == good_word[i]) {
            template[i] = '2';
            char_number[i]--;
        } else {
            template[i] = '0';
        }
        i++;
    }

    i = 0;
    while (good_word[i] != '\0') {
        if (good_word[i] != try[i] && char_number[i] > 0 && _count_char(good_word, try[i]) > 0) {
            template[i] = '1';
            char_number[i]--;
        }
        i++;
    }
}


int *init_nb_turn_result(int size) {
    int *nb_turn_result = malloc(sizeof(int) * (size + 1));

    int i = 0;
    while (i < size) {
        nb_turn_result[i] = 0;
        i++;
    }
    nb_turn_result[i] = -1;

    return nb_turn_result;
}


double calculate_average(int *nb_turn_result) {
    int i = 0;
    double sum = 0;
    double coef = 0;

    while (nb_turn_result[i] != -1) {
        sum += nb_turn_result[i] * (i + 1);
        coef += nb_turn_result[i];
        i++;
    }

    return sum / coef;
}


int main() {
    char *n = word_length();
    int word_length = atoi(n);

    char **paths = get_all_path();
    FILE *file = open_txt(paths[word_length]);

    // Initialize the dictionary
    char_node *dictionary = create_char_node();
    init_dictionary_tree(file, dictionary, word_length);

    // Init the template list
    linked_list_template *template_list = init_linked_list_template(word_length);

    char *template = malloc(sizeof(char) * (word_length + 1));
    template[word_length] = '\0';

    char *line = malloc(sizeof(char) * (word_length + 2));

    int opening_is_word;
    int turn_count;
    int *nb_turn_result = init_nb_turn_result(10);
    best_word *best;

    file = open_txt(paths[word_length]);

    while (fgets(line, word_length + 2, file)) {
        opening_is_word = 0;
        turn_count = 1;
        line[word_length] = '\0';

        char_node *dictionary_copy = copy_char_node(dictionary);

        // Get the best word for the given word length
        char *best_opening = get_best_opening(word_length);

        best = init_best_word(best_opening);
        best->score = -1;

        printf("Tested word %s, best word %s\n", line, best->word);

        // Calculate the template for the opening word
        calculate_wordle_template(template, line, best->word);

        if (_strcmp(line, best->word) == 0) {
            nb_turn_result[turn_count - 1]++;
            opening_is_word = 1;
            printf("Word found\n");
        } else {
            cut_char_node(dictionary_copy, template, best->word);
        }


        while (turn_count < 10 && opening_is_word == 0) {
            turn_count++;

            calculate_best_word(dictionary_copy, word_length, template_list, best);

            calculate_wordle_template(template, line, best->word);

            if (_strcmp(line, best->word) == 0) {
                nb_turn_result[turn_count - 1]++;
                printf("Word found\n");
                break;
            } else {
                cut_char_node(dictionary_copy, template, best->word);
            }
        }

        free_char_node(dictionary_copy);
    }

    printf("Average number of turns: %f\n", calculate_average(nb_turn_result));

    fclose(file);
    free_best_word(best);
    free_all_path(paths);
    free(template);
    free(line);
    return 1;
}
