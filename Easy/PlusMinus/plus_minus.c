#include <stdio.h>
int plus_minus(int *, int);

int main(int argc, char const *argv[])
{
    int size;
    scanf("%d", &size);
    int arr[size];
    for(int i=0;i<size;i++)
    {
        scanf("%d", &arr[i]);
    }
    plus_minus(arr, size);
    return 0;
}

int plus_minus(int * arr, int size)
{
    // zero counter
    float zero = 0.0;
    // positive counter
    float pos = 0.0;
    // negative counter
    float neg = 0.0;
    // loop through array to find num of zero, pos, neg vals
    for(int i=0;i<size;i++)
    {
        // take diff between element and 0
        int diff = 0 - arr[i];
        // if result is zero, inc zero counter 
        if(diff == 0)
        {
            zero++;
        }
        // if result is greater than zero, inc neg counter
        if(diff > 0)
        {
            neg++;
        }
        // if result is less than zero, inc pos counter
        if(diff < 0)
        {
            pos++;
        }
    }
    /*
    zero = zero/size;
    pos = pos/size;
    neg = neg/size;
    */
    printf("%.6f\n",pos/size);
    printf("%.6f\n",neg/size);
    printf("%.6f\n",zero/size);
    return 0;
}
