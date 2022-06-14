    //
// Created by Thibault Cheneviere on 30/05/2022.
//

#include "../includes/core_node.h"

// Functions to calculate the score of a word
// Core functions for the solver
void calculate_best_word(char_node *dictionary, int size, linked_list_template *template_list, best_word *best) {
    best->score = -1;

    char *path = malloc(sizeof(char) * (size + 1));
    path[size] = '\0';
    double_linked_list_node *node_next = dictionary->next;
    if (node_next != NULL) {
        double_linked_list_node_element *current_element = node_next->value;
        while (current_element != NULL) {
            calculate_best_word_recursive(dictionary, current_element->value, best, path, 0, template_list);
            current_element = current_element->next;
        }

    }

    free(path);
}


void calculate_best_word_recursive(char_node *root, char_node *node, best_word *best, char *path, int depth, linked_list_template *list_template) {
    if (node->next->value == NULL) {
        assert(depth == _strlen(path) - 1);
        path[depth++] = node->value;
        path[depth] = '\0';

        char *word = malloc(sizeof(char) * (depth + 1));
        _strcpy(word, path);

        double word_score = calculate_entropy(root, word, list_template);
        if (word_score > best->score) {
            _strcpy(best->word, word);
            best->score = word_score;
        }
        free(word);
        return;
    } else {
        path[depth] = node->value;
        double_linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL) {
            calculate_best_word_recursive(root, current_element->value, best, path, depth + 1, list_template);
            current_element = current_element->next;
        }
    }
}


// Cut functions
void cut_words_for_calculation(char_node *root, char *user_response, char *word) {
        assert(_strlen(user_response) == _strlen(word));

        int i = 0;
        while (user_response[i]) {
            if (user_response[i] == '0') {
                int j = 0;

                while (word[j] != '\0') {
                    if (!((word[j] == word[i] && user_response[j] == '2') || check_letter_with_position_one(word, user_response, word[i]))) {
                        cut_words_for_calculation_recursive(j + 1, 0, word[i], root, 0);
                    }

                    j++;
                }
            } else if (user_response[i] == '1' && (i + 1) < _strlen(word)) {
                cut_words_for_calculation_recursive(i + 1, 0, word[i], root, 0);
                cut_words_for_calculation_recursive(_strlen(word), 3, word[i], root, calculate_allowed_letter(i, word, user_response));
            }
            else {
                cut_words_for_calculation_recursive(i + 1, user_response[i] - 48, word[i], root, 0);
            }
            i++;
        }
}


void cut_words_for_calculation_recursive(int depth, int template_temper, char word_temper, char_node *dictionary, int allowed_letters) {
    if (depth == 0) {
        int word_temper_in_path;
        switch (template_temper) {
            case 0:
                if (word_temper == dictionary->value) {
                    dictionary->is_cuted = true;
                }
                break;
            case 1:
                word_temper_in_path = is_char_in_parent_char_node(dictionary, word_temper);
                if (word_temper == dictionary->value || word_temper_in_path == 0) {
                    dictionary->is_cuted = true;
                }
                break;
            case 2:
                if (word_temper != dictionary->value) {
                    dictionary->is_cuted = true;
                }
                break;
            case 3:
                word_temper_in_path = is_char_in_parent_char_node(dictionary, word_temper);
                if (word_temper_in_path != allowed_letters) {
                    dictionary->is_cuted = true;
                }
        }
        return;
    } else {
        double_linked_list_node *current_node_leaf = dictionary->next;
        if (current_node_leaf == NULL) {
            return;
        }
        double_linked_list_node_element *current_element = current_node_leaf->value;
        while (current_element != NULL && current_element->value != NULL) {
            cut_words_for_calculation_recursive(depth - 1, template_temper, word_temper, current_element->value, allowed_letters);
            current_element = current_element->next;
        }
    }
}


void cut_char_node(char_node *root, char *user_response, char *word) {
    assert(_strlen(user_response) == _strlen(word));

    int i = 0;
    while (user_response[i]) {
        if (user_response[i] == '0') {
            int j = 0;

            while (word[j] != '\0') {
                if (!((word[j] == word[i] && user_response[j] == '2') || check_letter_with_position_one(word, user_response, word[i]))) {
                    cut_char_node_recursive(j + 1, 0, word[i], root, 0);
                }

                j++;
            }
        } else if (user_response[i] == '1' && (i + 1) < _strlen(word)) {
            cut_char_node_recursive(i + 1, 0, word[i], root, 0);
            cut_char_node_recursive(_strlen(word), 3, word[i], root, calculate_allowed_letter(i, word, user_response));
        }
        else {
            cut_char_node_recursive(i + 1, user_response[i] - 48, word[i], root, 0);
        }
        i++;
    }

    clean_tree(root, _strlen(word));
}


void cut_char_node_recursive(int depth, int template_temper, char word_temper, char_node *dictionary, int allowed_letters) {
    assert(dictionary != NULL);

    if (depth == 0) {
        int word_temper_in_path;
        switch (template_temper) {
            case 0:
                if (word_temper == dictionary->value) {
                    remove_element_from_char_node(dictionary);
                }
                break;
            case 1:
                word_temper_in_path = is_char_in_parent_char_node(dictionary, word_temper);
                if (word_temper == dictionary->value || word_temper_in_path == 0) {
                    remove_element_from_char_node(dictionary);
                }
                break;
            case 2:
                if (word_temper != dictionary->value) {
                    remove_element_from_char_node(dictionary);
                }
                break;
            case 3:
                word_temper_in_path = is_char_in_parent_char_node(dictionary, word_temper);
                if (word_temper_in_path != allowed_letters) {
                    remove_element_from_char_node(dictionary);
                }
        }
        return;
    } else {
        double_linked_list_node *current_node_leaf = dictionary->next;
        if (current_node_leaf == NULL) {
            return;
        }
        double_linked_list_node_element *current_element = current_node_leaf->value;
        double_linked_list_node_element *temp_next;
        while (current_element != NULL && current_element->value != NULL) {
            temp_next = current_element->next;
            cut_char_node_recursive(depth - 1, template_temper, word_temper, current_element->value, allowed_letters);
            current_element = temp_next;
        }
    }
}


bool check_letter_with_position_one(char *word, char *template, char letter) {
    assert(_strlen(template) == _strlen(word));

    int i = 0;

    while (word[i]) {
        if (word[i] == letter && template[i] == '1') {
            return true;
        }
        i++;
    }

    return false;
}


void init_dictionary_tree(FILE *file, char_node *dictionary, int MAX_WORD_SIZE) {
    MAX_WORD_SIZE++;
    char *line = malloc(sizeof(char) * MAX_WORD_SIZE);

    while (fgets(line, MAX_WORD_SIZE, file)) {
        if (_strlen(line) == MAX_WORD_SIZE - 1) {
            add_word_to_char_node(dictionary, line);
        }
    }
    fclose(file);
}


// Function to use the best_word structure
best_word *init_best_word(char *word) {
    best_word *best = malloc(sizeof(best_word));
    best->word = malloc(sizeof(char) * _strlen(word) + 1);
    _strcpy(best->word, word);
    best->score = 0;
    return best;
}


void copy_best_word(best_word *dest, best_word *src) {
    _strcpy(dest->word, src->word);
    dest->score = src->score;
}


void free_best_word(best_word *best_word){
    free(best_word->word);
    free(best_word);
}

