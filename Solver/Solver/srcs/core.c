//
// Created by Thibault Cheneviere on 27/05/2022.
//

#include "../includes/core.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char **get_all_path() {
    char **paths = malloc(sizeof(char *) * 26);
    char *str_1 = "l_";
    char *str_2 = "_reponse.txt";

    for (int i = 0; i < 26; i++) {
        char *temp_num = malloc(sizeof(char) * 2);
        char *temp_buffer = malloc(sizeof(char) * 30);
        if (_asprintf(&temp_num, "%d", i) == -1) {
            perror("asprintf");
        } else {
            strcat(strcpy(temp_buffer, str_1), temp_num);
            strcat(temp_buffer, str_2);
            paths[i] = malloc(sizeof(char) * 30);
            strcpy(paths[i], temp_buffer);
        }

        free(temp_num);
        free(temp_buffer);
    }

    return paths;
}


void free_all_path(char **paths) {
    for (int i = 0; i < 26; i++) {
        free(paths[i]);
    }
    free(paths);
}


FILE* open_txt(char* path){
    char *complete_path = malloc(sizeof(char) * 80);
    strcpy(complete_path, "./Data/");
    strcat(complete_path, path);

    FILE *fp = fopen( complete_path , "r" );
    if(fp == NULL){
        perror("ERROR: couldn't open the file \n");
    }
    free(complete_path);
    return fp;
}


char* word_length(){
    FILE* fp = open_txt("wsolf.txt");

    const unsigned MAX_LENGTH = 256;
    char *line = malloc(sizeof(char) * MAX_LENGTH);

    fgets(line, MAX_LENGTH, fp);

    fclose(fp);
    return line;
}


// Function that return the word_length th line of the file best_opening.txt
char *get_best_opening(int word_length) {
    FILE *fp = open_txt("best_opening.txt");

    const unsigned MAX_LENGTH = 256;
    char *line = malloc(sizeof(char) * MAX_LENGTH);

    int i = 1;

    while (fgets(line, MAX_LENGTH, fp)) {
        if (i == word_length) {
            break;
        } else {
            i++;
        }
    }
    line[word_length] = '\0';

    fclose(fp);
    return line;
}


bool check_template_validity(char *template) {
    int i = 0;

    while (template[i] != '\0') {
        if (template[i] != '0' && template[i] != '1' && template[i] != '2') {
            return false;
        }
        i++;
    }

    return true;
}


bool check_template(char *user_response, int word_length) {
    if (user_response[0] == '-' && user_response[1] == '1') {
        printf("You exited program\n");
        return true;
    }

    if (_strlen(user_response) != word_length) {
        printf("You entered a wrong template : length error.\n");
        return true;
    }

    if (!check_template_validity(user_response)) {
        printf("You entered a wrong template : invalid characters.\n");
        return true;
    }

    return false;
}
