#include <stdio.h>

void main () {
        printf("|%050c|\n", 0x41424344);
        printf("|%030c|\n", 0x41424344);
        printf("|%013c|\n", 0x41424344);
}
