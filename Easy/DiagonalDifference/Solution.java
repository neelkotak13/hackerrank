/*
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, . The next lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

Constraints

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15

Explanation

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is absolute value function
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution
{

    public static int diagdiff(int[] arr,int n)
    {
        int diff;
        int p = 0;
        int s = 0;
        int counter = n-1;
        for(int i=0;i<=Math.pow(n,2);i+=n+1)
        {
            p += arr[i];
        }
        while(counter != n*n-1)
        {
            s += arr[counter];
            counter += n-1;
        }
        // for(int j =n-1;j<=Math.pow(n,2);j+=n-1)
        // {
        //     s += arr[j];
        // }
        // s -= arr[n*n-1];
        diff = p-s;
        if(diff < 0)
        {
            diff = -diff;
        }
        return diff;
    }
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n*n];
        for(int i=0;i<n*n;i++)
        {
            arr[i] = s.nextInt();
        }
        System.out.printf("%d",diagdiff(arr,n));
    }
}
