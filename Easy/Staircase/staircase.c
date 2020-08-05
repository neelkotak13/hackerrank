/********************

Problem: https://www.hackerrank.com/challenges/staircase/problem

input: integer less than 100
output: staircase of '#' where height is equal to input
********************/

#include <stdio.h>

int print_staircase(int);

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d",&n);
    print_staircase(n);
    return 0;
}

int print_staircase(int n)
{
    // step counter
    int step = 1;
    // loop n times
    for(int i=0;i<n;i++)
    {
        // num of spaces to put is n-1 for each line
        for(int j=0;j<n-step;j++)
        {
            printf(" ");
        }
        // num of the step is how many '#' are required
        for(int k=0;k<step;k++)
        {
            printf("#");
        }
        // increment to go to next step
        step++;
        // new line for next step
        printf("\n");
    }
    return 0;
}

