//
// Created by Thibault Cheneviere on 31/05/2022.
//

#ifndef SOLVER_CORE_TEMPLATE_H
#define SOLVER_CORE_TEMPLATE_H

#include "template_list.h"


linked_list_template *init_linked_list_template(int size);
void init_linked_template_list_recursive(linked_list_template *list, int depth, int *path, int size);

#endif //SOLVER_CORE_TEMPLATE_H
