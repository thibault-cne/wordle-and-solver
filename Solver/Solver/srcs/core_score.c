//
// Created by Thibault Cheneviere on 31/05/2022.
//

#include "../includes/core_score.h"


double calculate_entropy(char_node *root, char *word, linked_list_template *template_list) {
    double pre_dictionary_size = count_leaf_char_node(root, _strlen(word));
    double px;
    double entropy = 0;

    if (template_list->value == NULL) {
        return 0;
    } else {
        assert(template_list->template_size == _strlen(word));
        int length = template_list->template_size;

        linked_list_template_element *current_template = template_list->value;
        while (current_template != NULL) {
            cut_words_for_calculation(root, _int_to_string(current_template->value, length), word);

            px = (double) count_leaf_char_node(root, length) / pre_dictionary_size;
            assert(px >= 0 && px <= 1);
            if (px != 0) {
                entropy -= px * log2(px);
            } else {
                entropy += 0;
            }

            restore_char_node(root);
            current_template = current_template->next;
        }

        return entropy;
    }
}
