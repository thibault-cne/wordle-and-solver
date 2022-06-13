//
// Created by Thibault Cheneviere on 30/05/2022.
//

#ifndef SOLVER_LINKED_LIST_NODE_H
#define SOLVER_LINKED_LIST_NODE_H

#include <stdio.h>
#include <stdlib.h>

#include "char_node.h"

typedef struct _char_node char_node;

typedef struct _linked_list_node_element {
    char_node *value;
    struct _linked_list_node_element *next;
} linked_list_node_element;

typedef struct _linked_list_node {
    struct _linked_list_node_element *value;
} linked_list_node;


linked_list_node *create_linked_list_node();
void free_linked_list_node(linked_list_node *list);
void soft_free_linked_list_node(linked_list_node *list);

linked_list_node_element *create_linked_list_node_element(char_node *value);
void free_linked_list_node_element(linked_list_node_element *element);
void soft_free_linked_list_node_element(linked_list_node_element *element);

// Core functions to manipulate the linked list
void add_element_to_linked_list(linked_list_node *list, char_node *value);
void add_element_to_linked_list_element(linked_list_node_element *element, char_node *value);

linked_list_node_element *remove_element_from_linked_list(linked_list_node *list, char_node *element);
linked_list_node_element *remove_element_from_linked_list_element(linked_list_node_element *element, char_node *value);

linked_list_node_element *find_element_in_linked_list(linked_list_node *list, char_node *element);
linked_list_node_element *find_element_in_linked_list_element(linked_list_node_element *element, char_node *value);

#endif //SOLVER_LINKED_LIST_NODE_H
