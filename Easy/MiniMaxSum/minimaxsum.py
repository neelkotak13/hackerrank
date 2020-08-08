#!/usr/bin/env python3

import math
'''
Problem: https://www.hackerrank.com/challenges/mini-max-sum/
input: single line of 5 space separated integers
output: two space separated long integers denoting the respective minimum and maximum
        values that can be calculated by summing exactly four of the five integers

1. Sort the list by lowest to highest value
2. add the first 4 values, this is the minimum value
3. add the last 4 values, this is the maximum value
4. print the values to the screen
'''
def miniMaxSum(arr):
    arr.sort()
    min_val = 0
    max_val = 0
    for i in range(0,4):
        min_val = min_val + arr[i]
    for i in range(1,5):
        max_val = max_val + arr[i]
    print(min_val, max_val)
    return 0

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)


