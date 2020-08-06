#!/usr/bin/env python3

import math
'''
Problem: https://www.hackerrank.com/challenges/mini-max-sum/
input: single line of 5 space separated integers
output: two space separated long integers denoting the respective minimum and maximum
        values that can be calculated by summing exactly four of the five integers

1. find min value and max value in list and store in separate variables called min_val and max_val respectively
2. arrSum = sum of remaining values
3. min = sum + min; max = sum + max
4. print min and max values to screen
'''

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

def miniMaxSum(arr):
    # store min and max value, start it at the 0th index
    # store min and max value index, so no need to search for it later, started at 0th index
    min_val = arr[0]
    max_val = arr[0]
    min_index = 0
    max_index = 0
    # since starting with 0th value, only need to go through indexes 1-4
    for i in range(1,5):
        # if larger max value found, replace it and the index value
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        if arr[i] < min_val:
        # if smaller min value found, replace it and the index value
            min_val = arr[i]
            min_index = i
    # del max and min index values from array
    del arr[max_index]
    del arr[min_index]
    # sum of array with all, except index val
    arrSum = sum(arr)
    min_val = arrSum + min_val
    max_val = arrSum + max_val
    # print solution
    print(min_val,max_val)
    return 0

