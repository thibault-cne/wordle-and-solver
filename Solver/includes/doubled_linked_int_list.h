//
// Created by louiscleriot on 21/05/2022.
//

#ifndef SOLVER_DOUBLED_LINKED_INT_LIST_H
#define SOLVER_DOUBLED_LINKED_INT_LIST_H

#include <stdlib.h>
#include "double_linked_char_list.h"


double_linked_char_list *create_double_linked_int_list();
void add_element_to_double_linked_int_list(double_linked_char_list *list, int value);
void free_double_linked_int_list(double_linked_char_list *list);

#endif //SOLVER_DOUBLED_LINKED_INT_LIST_H
