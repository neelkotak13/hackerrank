#include <stdio.h>
int formingMagicSquare(int [3][3],int [3][3]);

int main(int argc, char const *argv[])
{
    int s[3][3];
    int t[3][3];
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++){
            scanf("%d",&s[i][j]);
            t[i][j] = s[i][j];
        }
    }

    printf(
    "\n%d %d %d\n%d %d %d\n%d %d %d\n",
    s[0][0],s[0][1],s[0][2],s[1][0],s[1][1],s[1][2],s[2][0],s[2][1],s[2][2]);

    formingMagicSquare(s,t);
    return 0;
}

int formingMagicSquare(int s[3][3], int t[3][3])
{
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            if(i==0)
            {
                if(j==0)
                {
                    s[i][j] = s[i+1][j];
                }
                if(j==1)
                {
                    s[i][j] = s[i][j-1];
                }
            }
            if(i==1)
            {
                if(j==0)
                {
                    s[i][j] = s[i-1][j];
                }
                if(j==1)
                {
                    continue;
                }
                else
                {
                    s[i][j] = s[i+1][j];
                }
            }
            if(i==2)
            {
                if(j==0)
                {
                    s[i][j] = s[i-1][j];
                }
                else
                {
                    s[i][j] = s[i][j-1];
                }
            }
        }
    }

    printf(
    "\n%d %d %d\n%d %d %d\n%d %d %d\n",
    s[0][0],s[0][1],s[0][2],s[1][0],s[1][1],s[1][2],s[2][0],s[2][1],s[2][2]);
    return 0;
}
