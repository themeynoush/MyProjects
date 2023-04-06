// define a function to print the english alphabet in lower case


#include <stdio.h>
void printEnglishAlphabet(void);
void printEnglishAlphabet(void)
{
    char letter;
    for (letter = 'a'; letter <= 'z'; letter++)
        printf("%c ", letter);
}


int main(void)
{
    printEnglishAlphabet();
    return 0;
}
