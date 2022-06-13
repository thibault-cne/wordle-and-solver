//
// Created by Groupe E-19 on 13/05/2022.
//
#include "../includes/core.h"
#include "../includes/core_node.h"
int main() {
    char* n = word_length();
    int word_length = atoi(n);

    char_node *dictionary = create_char_node();
    char **paths =get_all_path();
    FILE *file = open_txt(paths[word_length]);
    init_dictionary_tree(file, dictionary, word_length);
    char *template = malloc(sizeof(char) * (word_length + 1));
    best_word *best ;
    for (int i = 0; i < word_length; i++) {
        best = calculate_best_word(dictionary, word_length);
        printf("%s\n", best->word);
        fgets(template,word_length,stdin);
        fflush(stdin);
        cut_char_node(dictionary, template, best->word);
    }
    free_all_path(paths);
    free(template);
    free_char_node(dictionary);
    free_best_word(best);
    return 0;
}
