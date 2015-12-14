#include <stdio.h>

void foo(char * var)
{
    printf(var);
}

int main(int argc, const char *argv[])
{
    foo(argv[1]);
    return 0;
}
