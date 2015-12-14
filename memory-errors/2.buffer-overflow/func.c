#include <stdio.h>

void func3() {
    printf("this should never be called!\n");
}

void func2() {
    char name[4];

    gets(name);

    printf("func2 has been called\n");
}

void func1() {
    printf("func1 has been called.\n");
    func2();
}

int main(int argc, const char *argv[])
{
    func1();

    return 0;
}
