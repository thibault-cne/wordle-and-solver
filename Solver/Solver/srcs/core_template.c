//
// Created by Thibault Cheneviere on 31/05/2022.
//

#include "../includes/core_template.h"


linked_list_template *init_linked_list_template(int size) {
    linked_list_template *list = create_linked_list_template(size);

    int *path = malloc(sizeof(int) * size);
    init_linked_template_list_recursive(list, 0, path, size);
    free(path);

    return list;
}


void init_linked_template_list_recursive(linked_list_template *list, int depth, int *path, int size) {
    if (depth == size) {
        add_element_to_linked_list_template(list, path, size);
    } else {
        int i = 0;
        while (i < 3) {
            path[depth] = i;
            init_linked_template_list_recursive(list, depth + 1, path, size);
            i++;
        }
    }
}
