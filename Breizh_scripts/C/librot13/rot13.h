#pragma once
/*
 * ROT13 encoding library
 */

/**
 * This function will encode the provided string in-place. Only the letters will
 * be modified. Return value is a pointer to the modified string.
 */
extern char *rot13(char *input);


