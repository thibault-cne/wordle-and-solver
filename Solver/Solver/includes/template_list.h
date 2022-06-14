//
// Created by Thibault Cheneviere on 31/05/2022.
//

#ifndef SOLVER_TEMPLATE_LIST_H
#define SOLVER_TEMPLATE_LIST_H

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>


typedef struct _linked_list_template_element {
    int *value;
    struct _linked_list_template_element *next;
} linked_list_template_element;

typedef struct _linked_list_template {
    int template_size;
    struct _linked_list_template_element *value;
} linked_list_template;


linked_list_template *create_linked_list_template(int size);
void free_linked_list_template(linked_list_template *list);

linked_list_template_element *create_linked_list_template_element(int size);
void free_linked_list_template_element(linked_list_template_element *element);


// Core functions to manipulate the linked list
void add_element_to_linked_list_template(linked_list_template *list, int *value, int size);
void add_element_to_linked_list_template_element(linked_list_template_element *element, int *value, int size);


// Functions to display the linked list
void display_linked_list_template(linked_list_template *list);
void display_linked_list_template_element(linked_list_template_element *element, int size);


#endif //SOLVER_TEMPLATE_LIST_H
