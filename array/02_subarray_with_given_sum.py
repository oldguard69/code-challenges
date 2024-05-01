"""
https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

Given an unsorted array A of size N that contains only non negative integers, 
find a continuous sub-array that adds to a given number S and return the left
 and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray 
indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements 
left and right. In case no such subarray exists return an array consisting of element -1.

"""
from dataclasses import dataclass


@dataclass
class Testcase:
    input_arr: list[int]
    input_s: int
    output: list[int]


def subarray_with_given_sum(arr: list[int], s: int) -> list[int]:
    n = len(arr)
    if n == 1:
        if arr[0] == s:
            return [1]
        return [-1]
    
    i, j = 0, 1
    temp_s = arr[i] + arr[j]
    if temp_s == s:
        return [i+1, j+1]

    while i < n and j < n:
        if temp_s < s:
            j += 1
            temp_s += arr[j]
        elif temp_s > s:
            temp_s -= arr[i]
            i += 1
        elif temp_s == s:
            return [i+1, j+1]
        else:
            return [-1]


testcases = [
    Testcase([1,2,3,7,5], 12, [2, 4]),
    Testcase([1,2,3,4,5,6,7,8,9,10], 15, [1, 5]),
    Testcase([0], 0, [1, 1]),

]
for t in testcases:
    print(subarray_with_given_sum(t.input_arr, t.input_s), t.output)