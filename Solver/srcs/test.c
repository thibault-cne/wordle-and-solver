//
// Created by Thibault Cheneviere on 13/06/2022.
//

#include "../includes/core_node.h"

int main() {
    char_node *root = create_char_node();

    add_word_to_char_node(root, "hello");
    add_word_to_char_node(root, "world");
    add_word_to_char_node(root, "louis");
    add_word_to_char_node(root, "laury");
    add_word_to_char_node(root, "thibo");

    cut_words_for_calculation(root, "00101", "hello");

    printf("%d", count_leaf_char_node(root, _strlen("hello")));
    display_char_node(root);

    free_char_node(root);
    return 0;
}
