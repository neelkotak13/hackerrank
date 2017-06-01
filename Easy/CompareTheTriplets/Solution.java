import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
// takes 6 values 3 corresponding to alice, 3 to bob
  static int[] solve(int a0,int a1, int a2,int b0, int b1,int b2)
  {
      int[] tot = new int[2];
      int[] alice = new int[3];
      int[] bob = new int[3];
      tot[0] = 0;tot[1] = 0;
      alice[0] = a0;alice[1]=a1;alice[2]=a2;
      bob[0]=b0;bob[1]=b1;bob[2]=b2;
      // System.out.println(Arrays.toString(alice));
      //adds a point to alice if her number is higher, adds to bobs if his is higher, nothing if equal   
      for(int i = 0;i < 3;i++)
      {
          if(alice[i]>bob[i])
          {
              tot[0]++;
          }
          else if(alice[i]<bob[i])
          {
              tot[1]++;
          }
          else
          {
              continue;
          }
      }
      return tot;
  }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a0 = in.nextInt();
        int a1 = in.nextInt();
        int a2 = in.nextInt();
        int b0 = in.nextInt();
        int b1 = in.nextInt();
        int b2 = in.nextInt();
        int[] result = solve(a0, a1, a2, b0, b1, b2);
        // prints results
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i != result.length - 1 ? " " : ""));
        }
        System.out.println("");


    }
}
