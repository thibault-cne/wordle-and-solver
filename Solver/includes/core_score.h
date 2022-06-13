//
// Created by Thibault Cheneviere on 31/05/2022.
//

#ifndef SOLVER_CORE_SCORE_H
#define SOLVER_CORE_SCORE_H

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

#include "core_node.h"
#include "core_template.h"
#include "core_char.h"

double calculate_entropy(char_node *root, char *word, char_node *dictionary, linked_list_template *template_list);

#endif //SOLVER_CORE_SCORE_H
