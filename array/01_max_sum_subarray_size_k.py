"""
https://www.geeksforgeeks.org/window-sliding-technique/

Given an array of integers of size ‘n’, 
Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
"""
from dataclasses import dataclass

@dataclass
class Testcase:
    input_n: list[int]
    input_k: int
    output: int

test_cases = [
    Testcase([100, 200, 300, 400], 2, 700),
    Testcase([1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39),
    Testcase([2, 3], 3, None),
]


def find_max_sum(arr: list[int], k: int) -> int:
    arr_len = len(arr)
    if arr_len < k:
        return None
    
    start = 0
    end = k - 1
    result_sum = sum(arr[start:end+1])
    while end < arr_len - 1:
        temp_sump = result_sum - arr[start] + arr[end+1]
        if temp_sump > result_sum:
            result_sum = temp_sump
        start += 1
        end += 1
    return result_sum


def find_max_sum_2(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k:
        return None
    
    result_sum = sum(arr[:k])
    for i in range(n - k):
        temp_sum = result_sum - arr[i] + arr[i+k]
        result_sum = max(temp_sum, result_sum)
    return result_sum


for t in test_cases:
    print(find_max_sum_2(t.input_n, t.input_k), t.output)
