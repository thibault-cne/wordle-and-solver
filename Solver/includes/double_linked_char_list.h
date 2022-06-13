//
// Created by Groupe E-19 on 04/05/2022.
//

#ifndef TEST_SOLVER_DOUBLE_LINKED_CHAR_LIST_H
#define TEST_SOLVER_DOUBLE_LINKED_CHAR_LIST_H

#include "stdlib.h"
#include "stdio.h"


typedef struct double_linked_char_list_element double_linked_char_list_element;
struct double_linked_char_list_element {
    char *value;
    double_linked_char_list_element *next;
    double_linked_char_list_element *previous;
};


typedef struct double_linked_char_list double_linked_char_list;
struct double_linked_char_list {
    double_linked_char_list_element *head;
    double_linked_char_list_element *tail;
};


// double_linked_char_list functions
double_linked_char_list *create_double_linked_char_list();
void add_element_to_double_linked_char_list(double_linked_char_list *list, char *value);
void remove_element_from_double_linked_char_list(double_linked_char_list *list, double_linked_char_list_element *element);
void print_double_linked_char_list(double_linked_char_list *list);
void free_double_linked_char_list(double_linked_char_list *list);

#endif //TEST_SOLVER_DOUBLE_LINKED_CHAR_LIST_H
