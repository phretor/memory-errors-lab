#include <stdio.h>
#include <string.h>

int foo(int a, const char* b)
{
    char buf[12];

    strcpy(buf, b);

    printf("You have passed level %d: %s\n", a, b);

    return 0;
}

int main(int argc, const char *argv[])
{
    int a = 1;

    foo(a, argv[1]);

    return 0;
}
