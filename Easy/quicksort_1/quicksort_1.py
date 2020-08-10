#/usr/bin/env python3
'''
input:  first line contains n, the size of the array arr
        second line contains n space-separated integers describing arr. the first integer arr[0] is your pivot element

output: on a single line, print the partitioned numbers, each integer should be separated by a single space

solution:
        1.  create 3 arrays: left, equal, right
        2.  designate arr[0] as the partition
        3.  iterate through arr and compare the values
            to pivot value and place into respective array
        4.  concat the arrays in the order from left, equal, right
'''
def partition(arr):
    # pivot value
    pivot = arr[0]
    # empty arrays for left, right, and equal
    left = []
    equal = []
    right = []
    # sends items to respective lists... might write a version to do this in-place later
    for item in arr:
        if item == arr[0]:
            equal.append(item)
        if item > arr[0]:
            right.append(item)
        if item < arr[0]:
            left.append(item)
    # concat the lists together
    arr = left + equal + right
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = partition(arr)
    print(*result)
