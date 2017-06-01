// https://www.hackerrank.com/challenges/simple-array-sum?h_r=next-challenge&h_v=zen
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int sum = 0;
        int arr[] = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        for(int j=0;j < n;j++)
        {
            sum+=arr[j];
        }
        System.out.println(sum);
    }
}
