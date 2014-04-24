#include <stdio.h>
#include <stdlib.h>

int foo(int a, int b)
{
    int c = 14;

    c = (a + b) * c;

    return c;
}

int main(int argc, char * argv[])
{
    int avar;
    int bvar;
    int cvar;

    avar = atoi(argv[1]);
    bvar = atoi(argv[2]);
    cvar = foo(avar, bvar);

    printf("foo(%d, %d) = %d\n", avar, bvar, cvar);

    return 0;
}
