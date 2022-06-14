//
// Created by Thibault Cheneviere on 30/05/2022.
//

#include "../includes/char_node.h"


char_node *create_char_node() {
    char_node *node = malloc(sizeof(char_node));
    node->value = '&';
    node->parent = NULL;
    node->is_cuted = false;
    node->next = create_double_linked_list_node();

    return node;
}


void free_char_node(char_node *node) {
    if (node->next != NULL) {
        free_double_linked_list_node(node->next);
    }

    free(node);
}


// Core functions to manipulate the linked list
void add_element_to_char_node(char_node *node, char value) {
    char_node *element = create_char_node();
    element->value = value;
    element->parent = node;

    add_element_to_double_linked_list_node(node->next, element);
}


void remove_element_from_char_node(char_node *element) {
    if (element->parent != NULL) {
        remove_element_from_double_linked_list_node(element->parent->next, element);
    }
}


int count_leaf_char_node(char_node *node, int height) {
    if (node->next->value == NULL && height == 0) {
        if (node->is_cuted) {
            return 0;
        } else {
            return 1;
        }
    } else {
        int count = 0;
        double_linked_list_node_element *element = node->next->value;
        while (element != NULL && element->value != NULL) {
            if (element->value->is_cuted == false) {
                count += count_leaf_char_node(element->value, height - 1);
            }
            element = element->next;
        }
        return count;
    }
}


int char_node_height(char_node *node) {
    if (node->next->value == NULL) {
        return 0;
    } else {
        int max_height = 0;
        double_linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL && current_element->value != NULL) {
            int height = char_node_height(current_element->value);
            if (height > max_height) {
                max_height = height;
            }
            current_element = current_element->next;
        }
        return max_height + 1;
    }
}


// Extended functions to manipulate the char node
void clean_tree(char_node *root, int size) {
    if (root->next->value == NULL) {
        return;
    } else {
        int i = size - 1;

        while (i > 0) {
            double_linked_list_node_element *element = root->next->value;
            double_linked_list_node_element *temp_next;
            while (element != NULL && element->value != NULL) {
                temp_next = element->next;
                clean_tree_recursive(element->value, i - 1);
                element = temp_next;
            }
            i--;
        }
    }
}


void clean_tree_recursive(char_node *root, int depth) {
    if (depth == 0) {
        if (is_empty_double_linked_list_node(root->next)) {
            remove_element_from_char_node(root);
        }
    } else {
        double_linked_list_node_element *element = root->next->value;
        double_linked_list_node_element *temp_next;
        while (element != NULL && element->value != NULL) {
            temp_next = element->next;
            clean_tree_recursive(element->value, depth - 1);
            element = temp_next;
        }
    }
}


void restore_char_node(char_node *node) {
    if (node->is_cuted) {
        node->is_cuted = false;
    }

    if (node->next->value != NULL) {
        double_linked_list_node_element *element = node->next->value;
        while (element != NULL) {
            restore_char_node(element->value);
            element = element->next;
        }
    }
}


char_node *get_son_char_node(char_node *dictionary, char letter) {
    double_linked_list_node_element *current_node_leaf = dictionary->next->value;

    while (current_node_leaf != NULL && current_node_leaf->value != NULL) {
        if (current_node_leaf->value->value == letter) {
            return current_node_leaf->value;
        }

        current_node_leaf = current_node_leaf->next;
    }
    return NULL;
}


void add_word_to_char_node(char_node *dictionary, char* word) {
    assert(dictionary != NULL && word != NULL);

    char_node *currentNode = dictionary;

    if (word[0] != '\0') {
        char_node *node = get_son_char_node(currentNode, word[0]);
        if (node == NULL) {
            node = create_char_node();
            node->value = word[0];
            node->parent = currentNode;
            add_element_to_double_linked_list_node(currentNode->next, node);
        }

        node = get_son_char_node(currentNode, word[0]);
        add_word_to_char_node(node, word + 1);
    }
}


char_node *copy_char_node(char_node *node) {
    char_node *copy = create_char_node();

    char *path = malloc(sizeof(char) * 100);
    double_linked_list_node_element *current_element = node->next->value;
    while (current_element != NULL) {
        copy_char_node_recursive(copy, current_element->value, path, 0);
        current_element = current_element->next;
    }

    free(path);
    return copy;
}


void copy_char_node_recursive(char_node *copy, char_node *node, char *path, int depth) {
    if (node->next->value == NULL) {
        path[depth++] = node->value;
        path[depth] = '\0';
        add_word_to_char_node(copy, path);
        return;
    } else {
        path[depth] = node->value;
        double_linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL) {
            copy_char_node_recursive(copy, current_element->value, path, depth + 1);
            current_element = current_element->next;
        }
    }
}


int is_char_in_parent_char_node(char_node *node, char letter) {
    if (node == NULL || node->value == '&') {
        return 0;
    } else {
        if (node->value == letter) {
            return 1 + is_char_in_parent_char_node(node->parent, letter);
        } else {
            return is_char_in_parent_char_node(node->parent, letter);
        }
    }
}


// Function to print the char node
void display_char_node(char_node *node) {
    char *path = malloc(sizeof(char) * 100);

    double_linked_list_node_element *current_element = node->next->value;
    while (current_element != NULL && current_element->value != NULL) {
        display_char_node_path(current_element->value, path, 0);
        current_element = current_element->next;
    }
}


void display_char_node_path(char_node *node, char *path, int depth) {
    if (is_empty_double_linked_list_node(node->next)) {
        path[depth++] = node->value;
        path[depth] = '\0';

        int i = 0;
        while (i < depth) {
            printf("%c", path[i]);
            i++;
        }
        printf("\n");
        return;
    } else {
        path[depth] = node->value;
        double_linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL && current_element->value != NULL) {
            if (current_element->value->is_cuted == false) {
                display_char_node_path(current_element->value, path, depth + 1);
            }
            current_element = current_element->next;
        }
    }
}
