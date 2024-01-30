#include <stdio.h>
#include "rot13.h"

static char rot13b(char c, char basis)
{
    c = (((c - basis) + 13) % 26) + basis;
    return c;
}

char *rot13(char *input)
{
    char *ptr = input;

    if (input == NULL) {
        return NULL;
    }
    
    while (*ptr != '\0') {
        if('a' <= *ptr && *ptr <= 'z'){
            *ptr = rot13b(*ptr, 'a');
        } else if ('A' <= *ptr && *ptr <= 'Z') {
            *ptr = rot13b(*ptr, 'A');
        }
        
        ptr++;
    }
    
    return input;
}
