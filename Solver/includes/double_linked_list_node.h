//
// Created by Thibault Cheneviere on 30/05/2022.
//

#ifndef SOLVER_DOUBLE_LINKED_LIST_NODE_H
#define SOLVER_DOUBLE_LINKED_LIST_NODE_H

#include <stdio.h>
#include <stdlib.h>

#include "char_node.h"

typedef struct _char_node char_node;

typedef struct _double_linked_list_node_element {
    char_node *value;
    struct _double_linked_list_node_element *next;
    struct _double_linked_list_node_element *previous;
} double_linked_list_node_element;

typedef struct _double_linked_list_node {
    struct _double_linked_list_node_element *value;
} double_linked_list_node;


double_linked_list_node *create_double_linked_list_node();
void free_double_linked_list_node(double_linked_list_node *list);

double_linked_list_node_element *create_double_linked_list_node_element(char_node *value);
void free_double_linked_list_node_element(double_linked_list_node_element *element);

// Core functions to manipulate the linked list
void add_element_to_double_linked_list_node(double_linked_list_node *list, char_node *value);
void remove_element_from_double_linked_list_node(double_linked_list_node *list, char_node *element);
bool is_empty_double_linked_list_node(double_linked_list_node *list);

void display_double_linked_list_node(double_linked_list_node *list);

#endif //SOLVER_DOUBLE_LINKED_LIST_NODE_H
