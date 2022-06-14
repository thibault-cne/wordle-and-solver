//
// Created by Thibault Cheneviere on 30/05/2022.
//

#include "../includes/double_linked_list_node.h"


double_linked_list_node *create_double_linked_list_node() {
    double_linked_list_node *list = malloc(sizeof(double_linked_list_node));
    list->value = NULL;

    return list;
}


void free_double_linked_list_node(double_linked_list_node *list) {
    assert(list != NULL);

    if (list->value == NULL) {
        free(list);
    } else {
        double_linked_list_node_element *element = list->value;

        while (element != NULL) {
            double_linked_list_node_element *next = element->next;
            free_double_linked_list_node_element(element);
            element = next;
        }
    }
}


double_linked_list_node_element *create_double_linked_list_node_element(char_node *value) {
    double_linked_list_node_element *element = malloc(sizeof(double_linked_list_node_element));
    element->value = value;
    element->next = NULL;
    element->previous = NULL;
    return element;
}


void free_double_linked_list_node_element(double_linked_list_node_element *element) {
    assert(element != NULL);

    if (element->value != NULL) {
        free_char_node(element->value);
    }

    free(element);
}


// Core functions to manipulate the linked list
void add_element_to_double_linked_list_node(double_linked_list_node *list, char_node *value) {
    assert(value != NULL && list != NULL);

    double_linked_list_node_element *element = create_double_linked_list_node_element(value);
    if (list->value == NULL) {
        list->value = element;
    } else {
        element->next = list->value;
        list->value->previous = element;
        list->value = element;
    }
}


void remove_element_from_double_linked_list_node(double_linked_list_node *list, char_node *element) {

    double_linked_list_node_element *current = list->value;
    if (current->value == element) {
        list->value = current->next;
        free_double_linked_list_node_element(current);
    } else {
        while (current != NULL) {
            if (current->value == element) {
                if (current->previous != NULL) {
                    current->previous->next = current->next;
                }
                if (current->next != NULL) {
                    current->next->previous = current->previous;
                }

                free_double_linked_list_node_element(current);
                return;
            }
            current = current->next;
        }
    }
}


bool is_empty_double_linked_list_node(double_linked_list_node *list) {
    assert(list != NULL);

    return list->value == NULL;
}


void display_double_linked_list_node(double_linked_list_node *list) {
    assert(list != NULL);

    double_linked_list_node_element *element = list->value;
    while (element != NULL) {
        printf("%c", element->value->value);
        element = element->next;
    }
    printf("\n");
}
