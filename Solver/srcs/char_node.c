//
// Created by Thibault Cheneviere on 30/05/2022.
//

#include "../includes/char_node.h"


char_node *create_char_node() {
    char_node *node = malloc(sizeof(char_node));
    node->value = '&';
    node->next = create_linked_list_node();
    node->parent = NULL;
    return node;
}


void free_char_node(char_node *node) {
    if (node->next != NULL) {
        free_linked_list_node(node->next);
    }

    free(node);
}


// Core functions to manipulate the linked list
char_node *add_element_to_char_node(char_node *node, char value) {
    char_node *element = create_char_node();
    element->value = value;
    element->parent = node;
    add_element_to_linked_list(node->next, element);

    return element;
}


void add_char_node_to_char_node(char_node *node, char_node *element) {
    if (element->parent != NULL) {
        add_element_to_linked_list(element->parent->next, element);
    } else {
        element->parent = node;
        add_element_to_linked_list(node->next, element);
    }
}


linked_list_node_element *remove_element_from_char_node(char_node *element) {
    linked_list_node_element *removed_element;
    if (element->parent != NULL) {
        removed_element = remove_element_from_linked_list(element->parent->next, element);
    } else {
        return NULL;
    }
    return removed_element;
}


int count_leaf_char_node(char_node *node) {
    if (node->next->value == NULL) {
        return 1;
    } else {
        int count = 0;
        linked_list_node_element *element = node->next->value;
        while (element != NULL) {
            count += count_leaf_char_node(element->value);
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
        linked_list_node_element *current_element = node->next->value;
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
void cut_and_save_char_node(char_node *element, linked_list_node *list) {
    if (!element->value) {
        return;
    }
    linked_list_node_element *removed_element = remove_element_from_char_node(element);
    if (removed_element != NULL) {
        add_element_to_linked_list(list, removed_element->value);
    } else {
        (void) list;
        printf("Error: element not found in the linked list\n");
    }
}


void restore_char_node(char_node *node, linked_list_node *list) {
    if (list->value == NULL) {
        return;
    } else {
        linked_list_node_element *current_element = list->value;
        while (current_element != NULL) {
            add_char_node_to_char_node(node, current_element->value);
            current_element = current_element->next;
        }
    }
}


char_node *get_son_char_node(char_node *dictionary, char letter) {
    linked_list_node_element *current_node_leaf = dictionary->next->value;

    while (current_node_leaf != NULL && current_node_leaf->value != NULL) {
        if (current_node_leaf->value->value == letter) {
            return current_node_leaf->value;
        } else {
            current_node_leaf = current_node_leaf->next;
        }
    }
    return NULL;
}


void add_word_to_char_node(char_node *dictionary, char* word) {
    char_node *current_node = dictionary;
    char_node *current_son;
    int i = 0;
    while (word[i] != '\0') {
        current_son = get_son_char_node(current_node, word[i]);
        if (current_son == NULL) {
            current_node = add_element_to_char_node(current_node, word[i]);
        } else {
            current_node = current_son;
        }
        i++;
    }
    current_son = get_son_char_node(current_node, word[i]);
    if (current_son == NULL) {
        add_element_to_char_node(current_node, word[i]);
    }
}


char_node *copy_char_node(char_node *node) {
    char_node *copy = create_char_node();

    char *path = malloc(sizeof(char) * 100);
    linked_list_node_element *current_element = node->next->value;
    while (current_element != NULL) {
        copy_char_node_recursive(copy, current_element->value, path, 0);
        current_element = current_element->next;
    }

    free(path);
    return copy;
}


void copy_char_node_recursive(char_node *copy, char_node *node, char *path, int depth) {
    if (node->next->value == NULL) {
        path[depth] = '\0';
        add_word_to_char_node(copy, path);
        return;
    } else {
        path[depth] = node->value;
        linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL) {
            copy_char_node_recursive(copy, current_element->value, path, depth + 1);
            current_element = current_element->next;
        }
    }
}


int is_char_in_parent_char_node(char_node *node, char letter) {
    if (node->value == '&') {
        return 0;
    } else {
        if (node->value == letter) {
            return 1;
        } else {
            return is_char_in_parent_char_node(node->parent, letter);
        }
    }
}


int is_char_in_children_char_node(char_node *node, char letter) {
    if (node->next->value == NULL) {
        return 0;
    } else {
        linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL) {
            if (current_element->value->value == letter) {
                return 1;
            } else {
                if (is_char_in_children_char_node(current_element->value, letter)) {
                    return 1;
                }
            }
            current_element = current_element->next;
        }
        return 0;
    }
}


// Function to print the char node
void display_char_node(char_node *node) {
    char *path = malloc(sizeof(char) * 100);

    linked_list_node_element *current_element = node->next->value;
    while (current_element != NULL && current_element->value != NULL) {
        display_char_node_path(current_element->value, path, 0);
        current_element = current_element->next;
    }
}


void display_char_node_path(char_node *node, char *path, int depth) {
    if (node->next->value == NULL) {
        int i = 0;
        while (i < depth) {
            printf("%c", path[i]);
            i++;
        }
        printf("\n");
        return;
    } else {
        path[depth] = node->value;
        linked_list_node_element *current_element = node->next->value;
        while (current_element != NULL && current_element->value != NULL) {
            display_char_node_path(current_element->value, path, depth + 1);
            current_element = current_element->next;
        }
    }
}
