"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest 
substring without repeating characters.
"""
from dataclasses import dataclass

@dataclass
class Testcase:
    input_s: str
    output: int



def longest_substr_without_repeating(s: str) -> int:
    print(s)
    n = len(s)
    match n:
        case 0:
            return 0
        case 1:
            return 1
    
    chars = set()
    i, j = 0, 0
    temp_max = 0
    result_max = 0
    while i < n and j < n:
        # print(s[i], s[j])
        if s[j] not in chars:
            chars.add(s[j])
            j += 1
            temp_max += 1
            result_max = max(temp_max, result_max)
        else:
            chars.remove(s[i])
            i += 1
            temp_max -= 1
        # print(chars)
    return result_max

ts = [
    Testcase("abcabcbb", 3),
    Testcase("bbbbb", 1),
    Testcase("abcc", 3)
]
for t in ts:
    print(longest_substr_without_repeating(t.input_s), t.output)
   

