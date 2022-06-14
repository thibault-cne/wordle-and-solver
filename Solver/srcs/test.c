//
// Created by Thibault Cheneviere on 13/06/2022.
//

#include "../includes/core_node.h"
#include "../includes/core.h"

int main() {
    char **path = get_all_path();


    char_node *root = create_char_node();

    FILE *file = open_txt(path[5]);

    init_dictionary_tree(file, root, 5);

    char_node *copy = copy_char_node(root);

    display_char_node(copy);

    free_all_path(path);
    free_char_node(root);
    return 0;
}
