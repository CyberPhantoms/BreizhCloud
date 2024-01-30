#include <rot13.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Usage: %s \"Message to encode\"\n", argv[0]);
        return 1;
    }
    
    fprintf(stdout, "%s\n", rot13(argv[1]));

    return 0;
}
