// define a function to print the english alphabet in lower case
#include <stdio.h>
void printEnglishAlphabet(void);
int main(void)
{
    printEnglishAlphabet();
    return 0;
}
void printEnglishAlphabet(void)
{
    char letter;
    for (letter = 'a'; letter <= 'z'; letter++)
        printf("%c ", letter);
    printf(" ");
}

