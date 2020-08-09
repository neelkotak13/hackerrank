#!/usr/bin/env python3

'''
Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

input:  first line contains a single integer n, denoting the number od candles on the cake
        the second line contains n space-separated integers, where each integer i describes
        the height of candle i.

output: return the number of candles that can be blown out on a new line 

solution:
    1. take input and get number of candles to be blown out and place in array
    2. iterate through array and find tallest candle height
    3. iterate through array again and count instances of the height in array
    4. print that value to screen
'''

def cakeCandles(arr):
    # count of candles that will be blown out, will be returned, starts at 0
    count = 0
    # set max candle value to 1st element initially
    maxCandle = arr[0]
    # 1st iteration to find tallest candle size
    for item in arr:
        if item > maxCandle:
            maxCandle = item
    # 2nd iteration to count instances of candle
    for item in arr:
        if item == maxCandle:
            count = count + 1
    return count

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cakeCandles(arr)
    print(result)
