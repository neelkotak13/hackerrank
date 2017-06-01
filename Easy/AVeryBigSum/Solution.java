import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
// calculates sum from inputted array of longs
    public static long sum(long[] arr)
    {
        long sum = 0;
        // adds values in array
        for(int i = 0;i<arr.length;i++)
        {
            sum+=arr[i];
        }
        return sum;
    }
    public static void main(String[] args) {
        // Waits for user input
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // creates array of longs
        long arr[] = new long[n];
        // adds input to array
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextLong();
        }
        // prints result
        System.out.printf("%d\n",sum(arr));
    }
}
