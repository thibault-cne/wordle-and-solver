//
// Created by Thibault Cheneviere on 31/05/2022.
//

#include "../includes/core_score.h"


double calculate_entropy(char_node *root, char *word, char_node *dictionary, linked_list_template *template_list) {
    int pre_dictionary_size = count_leaf_char_node(root);
    double px;
    double information;

    if (template_list->value == NULL) {
        return 0;
    } else {
        assert(template_list->template_size == _strlen(word));
        int length = template_list->template_size;

        char temper;
        int template_temper;

        linked_list_node *cut_nodes = create_linked_list_node();

        linked_list_template_element *current_template = template_list->value;
        while (current_template != NULL) {
            int i = 0;
            while ( i < length ) {
                temper = word[i];
                template_temper = current_template->value[i];

                // We verify that the node has enough height to go to depth i + 1
                if ((i + 1) > char_node_height(root)) {
                    break;
                }
                cut_words_for_calculation(i + 1, template_temper, temper, root, cut_nodes);
                i++;
            }
            if ((i + 1) > char_node_height(root)) {
                break;
            }
            current_template = current_template->next;
        }

        int post_dictionary_size = count_leaf_char_node(root);
        restore_char_node(dictionary, cut_nodes);
        soft_free_linked_list_node(cut_nodes);

        px = (double) post_dictionary_size / pre_dictionary_size;

        // Verify if px is between 0 and 1
        assert(px >= 0 && px <= 1);

        if (px == 1 || px == 0) {
            return 0;
        } else {
            information = -log2(px);
            return information * px;
        }
    }
}
