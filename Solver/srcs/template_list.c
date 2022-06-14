//
// Created by Thibault Cheneviere on 31/05/2022.
//

#include "../includes/template_list.h"


linked_list_template *create_linked_list_template(int size) {
    linked_list_template *list = malloc(sizeof(linked_list_template));
    list->template_size = size;
    list->value = NULL;
    return list;
}


void free_linked_list_template(linked_list_template *list) {
    linked_list_template_element *element = list->value;
    while (element != NULL) {
        linked_list_template_element *next = element->next;
        free_linked_list_template_element(element);
        element = next;
    }

    free(list);
}


linked_list_template_element *create_linked_list_template_element(int size) {
    linked_list_template_element *element = malloc(sizeof(linked_list_template_element));
    element->value = malloc(sizeof(int) * size);
    element->next = NULL;
    return element;
}


void free_linked_list_template_element(linked_list_template_element *element) {
    free(element->value);
    free(element);
}


// Core functions to manipulate the linked list
void add_element_to_linked_list_template(linked_list_template *list, int *value, int size) {
    assert(size == list->template_size);

    if (list->value == NULL) {
        linked_list_template_element *element = create_linked_list_template_element(size);
        int i = 0;
        while (i < size) {
            element->value[i] = value[i];
            i++;
        }
        list->value = element;
    } else {
        add_element_to_linked_list_template_element(list->value, value, size);
    }
}


void add_element_to_linked_list_template_element(linked_list_template_element *element, int *value, int size) {
    if (element->next == NULL) {
        linked_list_template_element *new_element = create_linked_list_template_element(size);
        int i = 0;
        while (i < size) {
            new_element->value[i] = value[i];
            i++;
        }
        element->next = new_element;
    } else {
        add_element_to_linked_list_template_element(element->next, value, size);
    }
}


// Function to display the linked list
void display_linked_list_template(linked_list_template *list) {
    if (list->value != NULL) {
        display_linked_list_template_element(list->value, list->template_size);
    }
}


void display_linked_list_template_element(linked_list_template_element *element, int size) {
    if (element->next != NULL) {
        display_linked_list_template_element(element->next, size);
    }

    int i = 0;
    while (i < size) {
        printf("%d ", element->value[i]);
        i++;
    }
    printf("\n");
}
