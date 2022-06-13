//
// Created by louiscleriot on 21/05/2022.
//

#include "../includes/doubled_linked_int_list.h"
double_linked_int_list *create_double_linked_int_list() {
    double_linked_int_list *list = malloc(sizeof(double_linked_int_list));
    list->head = NULL;
    list->tail = NULL;
    return list;
}
void add_element_to_double_linked_int_list(double_linked_int_list *list, int value) {
    double_linked_int_list_element *element = malloc(sizeof(double_linked_int_list_element));
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
void free_double_linked_int_list(double_linked_int_list *list) {
    double_linked_int_list_element *element = list->head;
    while (element != NULL) {
        double_linked_int_list_element *next = element->next;
        free(element);
        element = next;
    }
    free(list);
}