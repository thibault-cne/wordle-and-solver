//
// Created by Thibault Cheneviere on 31/05/2022.
//

#ifndef SOLVER_CORE_CHAR_H
#define SOLVER_CORE_CHAR_H

#include <stdio.h>
#include <assert.h>
#include <stdarg.h>
#include <stdlib.h>

int _strlen(char *str);
void _strcpy(char *dest, char *src);
int _strcmp(char *str1, char *str2);
int _asprintf (char **buf, const char *fmt, ...);
int _count_char(char *str, char c);
int *_count_all_char(char *str);

char *_int_to_string(int *value, int size);

int calculate_allowed_letter(int index, char *word, char *template);

#endif //SOLVER_CORE_CHAR_H
