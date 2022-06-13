//
// Created by Thibault Cheneviere on 04/05/2022.
//

#include "../includes/double_linked_char_list.h"


double_linked_char_list *create_double_linked_char_list() {
    double_linked_char_list *list = malloc(sizeof(double_linked_char_list));
    list->head = NULL;
    list->tail = NULL;
    return list;
}


void add_element_to_double_linked_char_list(double_linked_char_list *list, char *value) {
    double_linked_char_list_element *element = malloc(sizeof(double_linked_char_list_element));
    element->value = value;
    element->next = NULL;
    element->previous = NULL;
    if (list->head == NULL) {
        list->head = element;
        list->tail = element;
    } else {
        list->tail->next = element;
        element->previous = list->tail;
        list->tail = element;
    }
}


void remove_element_from_double_linked_char_list(double_linked_char_list *list, double_linked_char_list_element *element) {
    if (element->previous != NULL) {
        element->previous->next = element->next;
    } else {
        list->head = element->next;
    }
    if (element->next != NULL) {
        element->next->previous = element->previous;
    } else {
        list->tail = element->previous;
    }
    free(element);
}


void print_double_linked_char_list(double_linked_char_list *list) {
    double_linked_char_list_element *element = list->head;
    printf("[ ");
    while (element != NULL) {
        if (element->next != NULL) {
            printf("%s, ", element->value);
        } else {
            printf("%s", element->value);
        }
        element = element->next;
    }
    printf(" ]\n");
}


void free_double_linked_char_list(double_linked_char_list *list) {
    double_linked_char_list_element *element = list->head;
    while (element != NULL) {
        double_linked_char_list_element *next = element->next;
        free(element);
        element = next;
    }
    free(list);
}
