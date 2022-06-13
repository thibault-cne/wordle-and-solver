//
// Created by Thibault Cheneviere on 30/05/2022.
//

#ifndef SOLVER_CHAR_NODE_H
#define SOLVER_CHAR_NODE_H

#include <stdio.h>
#include <stdlib.h>

#include "linked_list_node.h"

typedef struct _linked_list_node linked_list_node;
typedef struct _linked_list_node_element linked_list_node_element;


typedef struct _char_node {
    char value;
    linked_list_node *next;
    struct _char_node *parent;
} char_node;


// Common functions to use the char node
char_node *create_char_node();
void free_char_node(char_node *node);


// Core functions to manipulate the char node
char_node *add_element_to_char_node(char_node *node, char value);
void add_char_node_to_char_node(char_node *node, char_node *element);
linked_list_node_element *remove_element_from_char_node(char_node *element);
int count_leaf_char_node(char_node *node);
int char_node_height(char_node *node);

// Extended functions to manipulate the char node
void cut_and_save_char_node(char_node *element, linked_list_node *list);
void restore_char_node(char_node *node, linked_list_node *list);
char_node *get_son_char_node(char_node *dictionary, char letter);
void add_word_to_char_node(char_node *dictionary, char* word);
char_node *copy_char_node(char_node *node);
void copy_char_node_recursive(char_node *copy, char_node *node, char *path, int depth);
int is_char_in_parent_char_node(char_node *node, char letter);
int is_char_in_children_char_node(char_node *node, char letter);

// Functions to display the char node
void display_char_node(char_node *node);
void display_char_node_path(char_node *node, char *path, int depth);

#endif //SOLVER_CHAR_NODE_H
