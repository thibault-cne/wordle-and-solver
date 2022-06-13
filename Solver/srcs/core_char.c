//
// Created by Thibault Cheneviere on 31/05/2022.
//

#include "../includes/core_char.h"


int _strlen(char *str) {
    int i = 0;
    while (str[i] != '\0') {
        i++;
    }
    return i;
}


void _strcpy(char *dest, char *src) {
    assert(dest != NULL);
    assert(src != NULL);

    int i = 0;
    while (src[i]) {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}


int _strcmp(char *str1, char *str2) {
    assert(str1 != NULL);
    assert(str2 != NULL);

    int i = 0;

    while (str1[i]) {
        if (str1[i] != str2[i]) {
            return 1;
        }
        i++;
    }

    return 0;
}


int _asprintf (char **buf, const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    int size = vsnprintf(NULL, 0, fmt, args);
    va_end(args);

    *buf = malloc(sizeof(char) * (size + 1));
    va_start(args, fmt);
    vsnprintf(*buf, size + 1, fmt, args);
    va_end(args);

    return size;
}


int _count_char(char *str, char c) {
    assert(str != NULL);

    int i = 0;
    int count = 0;
    while (str[i]) {
        if (str[i] == c) {
            count++;
        }
        i++;
    }
    return count;
}


int *_count_all_char(char *str) {
    assert(str != NULL);

    int *count = malloc(sizeof(int) * (_strlen(str) + 1));
    int i = 0;

    while (str[i]) {
        count[i] = _count_char(str, str[i]);
        i++;
    }
    count[i] = -1;

    return count;
}
