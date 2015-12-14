#include <stdio.h>
#include <string.h>

int authenticate() {
    //dummy function that returns always false
    return 0;
}

void check_password () {
    int check;
    char pass[16];

    check = authenticate();
    gets(pass);

    if (check)
        printf("Welcome!\n");
    else {
        printf("Failed!\n");
    }
}

int main(int argc, const char *argv[])
{
    check_password();

    return 0;
}
