#include <stdio.h>

void test(char *arg) {
    char buf[256];

    snprintf(buf, 250, arg);
    printf("buffer: %s\n", buf);
}

int main (int argc, char* argv[]) {
    test(argv[1]);
    return 0;
}
