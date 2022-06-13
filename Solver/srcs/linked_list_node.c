//
// Created by Thibault Cheneviere on 30/05/2022.
//

#include "../includes/linked_list_node.h"


linked_list_node *create_linked_list_node() {
    linked_list_node *list = malloc(sizeof(linked_list_node));
    list->value = NULL;
    return list;
}


void free_linked_list_node(linked_list_node *list) {
    if (list->value != NULL) {
        free_linked_list_node_element(list->value);
    }

    free(list);
}


void soft_free_linked_list_node(linked_list_node *list) {
    if (list->value != NULL) {
        soft_free_linked_list_node_element(list->value);
    }

    free(list);
}


linked_list_node_element *create_linked_list_node_element(char_node *value) {
    linked_list_node_element *element = malloc(sizeof(linked_list_node_element));
    element->value = value;
    element->next = NULL;
    return element;
}


void free_linked_list_node_element(linked_list_node_element *element) {
    if (element->next != NULL) {
        free_linked_list_node_element(element->next);
    }

    if (element->value != NULL) {
        free_char_node(element->value);
    }

    free(element);
}


void soft_free_linked_list_node_element(linked_list_node_element *element) {
    if (element->next != NULL) {
        soft_free_linked_list_node_element(element->next);
    }

    free(element);
}


// Core functions to manipulate the linked list
void add_element_to_linked_list(linked_list_node *list, char_node *value) {
    if (list->value == NULL) {
        linked_list_node_element *element = create_linked_list_node_element(value);
        list->value = element;
    } else {
        add_element_to_linked_list_element(list->value, value);
    }
}


void add_element_to_linked_list_element(linked_list_node_element *element, char_node *value) {
    if (element->next == NULL) {
        linked_list_node_element *new_element = create_linked_list_node_element(value);
        element->next = new_element;
    } else {
        add_element_to_linked_list_element(element->next, value);
    }
}


linked_list_node_element *remove_element_from_linked_list(linked_list_node *list, char_node *element) {
    if (list->value == NULL) {
        return NULL;
    }

    if (list->value->value == element) {
        linked_list_node_element *removed_element = list->value;
        list->value = removed_element->next;
        return removed_element;
    } else {
        return remove_element_from_linked_list_element(list->value, element);
    }
}


linked_list_node_element *remove_element_from_linked_list_element(linked_list_node_element *element, char_node *value) {
    if (element->next == NULL) {
        return NULL;
    }

    if (element->next->value == value) {
        linked_list_node_element *removed_element = element->next;
        element->next = element->next->next;
        return removed_element;
    } else {
        return remove_element_from_linked_list_element(element->next, value);
    }
}


linked_list_node_element *find_element_in_linked_list(linked_list_node *list, char_node *element) {
    if (list->value == NULL) {
        return NULL;
    }

    if (list->value->value == element) {
        return list->value;
    } else {
        return find_element_in_linked_list_element(list->value, element);
    }
}


linked_list_node_element *find_element_in_linked_list_element(linked_list_node_element *element, char_node *value) {
    if (element->next == NULL) {
        return NULL;
    }

    if (element->next->value == value) {
        return element->next;
    } else {
        return find_element_in_linked_list_element(element->next, value);
    }
}
