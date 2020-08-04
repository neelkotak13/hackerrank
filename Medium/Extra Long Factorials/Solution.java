/*
You are given an integer N. Print the factorial of this number.

Input
Input consists of a single integer N,  where 1 <= N ,= 100.

Output
Print the factorial of N.

*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// At first I thought of using long, but... it doesnt work for larger numbers, looked at hint and did research, should probably do more research
public class Solution
{
    public static BigInteger factorial(int n)
    {
        // creates big integer and sets its value to n
        BigInteger fact = new BigInteger(Integer.toString(n));
        // creates counter and sets value to n-1
        int counter = n-1;
        // multiplies values to fact and decrements counter, giving us factorial of n when counter is 0
        while(counter != 0)
        {
            fact = fact.multiply(BigInteger.valueOf(counter));
            counter--;
            // System.out.printf("%d",counter);
        }
        return fact;
    }
    public static void main(String args[])
    {
        // user input and prints output
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        System.out.printf("%d\n",factorial(n));
    }
}
