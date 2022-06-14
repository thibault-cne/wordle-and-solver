//
// Created by Groupe E-19 on 13/05/2022.
//

#include "../includes/core_score.h"
#include "../includes/core.h"

int main() {
    // Create the dictionary
    char_node *dictionary = create_char_node();

    // Get all path for .txt files
    char **all_path = get_all_path();

    // Get the word length needed
    char *file_word_length = word_length();
    int word_length = atoi(file_word_length);

    // Init the user response holder and turn count
    int turn_count = 0;
    char *user_response = malloc(sizeof(char) * (word_length + 1));
    user_response[word_length] = '\0';

    char *best_response = malloc(sizeof(char) * (word_length + 1));
    int i = 0;
    while (i < word_length) {
        best_response[i] = '2';
        i++;
    }
    best_response[word_length] = '\0';

    // Init the dictionary with the good .txt file
    FILE *file = open_txt(all_path[word_length]);
    init_dictionary_tree(file, dictionary, word_length);

    // Init the template list
    linked_list_template *template_list = init_linked_list_template(word_length);

    best_word *best = malloc(sizeof(best_word));
    best->score = -1;
    best->word = get_best_opening(word_length);

    // First turn
    printf("------------------------------------------------------\n\n");

    printf("Best word : %s with a score of %f \n\n", best->word, best->score);

    printf("Enter template response in format nnnnn (ex : 11111) : ");
    fgets(user_response, word_length + 1, stdin);
    fflush(stdin);

    // Check if the user response is a valid response
    if (check_template(user_response, word_length)) {
        // Put turn_count > 5 to end the program
        turn_count = 6;
    } else if (_strcmp(user_response, best_response) == 0) {
        printf("You won !!\n");
        // Put turn_count > 5 to end the program
        turn_count = 6;
    } else {
        cut_char_node(dictionary, user_response, best->word);
        display_char_node(dictionary);
    }


    while (turn_count < 5) {
        turn_count++;

        calculate_best_word(dictionary, word_length, template_list, best);
        printf("------------------------------------------------------\n\n");

        printf("Best word : %s with a score of %f \n\n", best->word, best->score);

        printf("Enter template response in format nnnnn (ex : 11111) : ");
        fgets(user_response, word_length + 1, stdin);
        fflush(stdin);
        
        // Check if the user response is a valid response
        if (check_template(user_response, word_length)) {
            break;
        }

        if (_strcmp(user_response, best_response) == 0) {
            printf("You won !!\n");
            break;
        } else {
            cut_char_node(dictionary, user_response, best->word);
            display_char_node(dictionary);
        }
    }

    // Free all the allocated memory
    free_linked_list_template(template_list);
    free_best_word(best);
    free_all_path(all_path);
    free(user_response);
    free_char_node(dictionary);
    return 0;
}
