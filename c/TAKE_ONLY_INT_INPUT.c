// C program for the above approach
#include <stdio.h>
int getIntegerOnly();

// Driver Code
int main()
{
    int x = 0;
    x = getIntegerOnly();
    printf("\nvalue entered is: %d", x);
}

// Function to check if the user
// entered value is integer or not

int getIntegerOnly()
{
    int num = 0, ch;
AGAIN:
    printf(" \n \n Enter the input: ");
    do
    {
        ch = getchar();

        // Checks the ASCII code of '
        // digits 0 to 9
        if (ch >= 48 && ch <= 57)
        {
            printf("%c", ch);

            // To make a digit
            num = num * 10 + (ch - 48);
        }
        
        if (ch == 0)
        {
            printf(" \n\nPlease Input numeric values only!!!!");
            goto AGAIN;
        }

        // 13 is carriage return it breaks
        // and return the input
        if (ch == '\n')
            break;
    } while (1);

    return (num);
}
