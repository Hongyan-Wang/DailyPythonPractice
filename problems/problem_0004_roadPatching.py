"""
# Task 2 — Road Patching

## Problem

There is a road consisting of N segments, numbered from 0 to N-1, represented by a string `S`. Segment `S[K]` may contain a pothole, denoted by a single uppercase `"X"`, or may be a good segment without any potholes, denoted by a single dot `"."`.

The road fixing machine can patch over **three consecutive segments** at once with asphalt and repair all the potholes located within each of those three segments. Good or already repaired segments remain good after patching them.

Your task is to compute the **minimum number of patches** required to repair all the potholes in the road.

Write a function:

```python
def solution(S)
```

that, given a string `S` of length N, returns the minimum number of patches required to repair all the potholes.

## Examples

1. Given `S = ".X..X"`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 2-4.
2. Given `S = "X.XXXXX."`, your function should return **3**. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
3. Given `S = "XX.XXX.."`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 3-5.
4. Given `S = "XXXX"`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 1-3.

## Assumptions

- N is an integer within the range [3..100,000]
- String S consists only of the characters `"."` and `"X"`

"""


import pytest 

def solution(S):
    # Approach: Greedy algorithm. 
    
    # Args:
    # S: a string consisting of characters 'X' and '.' where 'X' represents a pothole and '.' represents a smooth road.
    # Returns:
    # An integer representing the minimum number of patches needed to cover all the potholes in the road.

    # Time complexity: O(N) where N is the length of the input string S, since we are iterating through the string once.
    # Space complexity: O(1) since we are using a constant amount of space to store the number of patches.

    # Corner cases:
    # - If S is empty, the function should return 0 since there are no potholes to patch.
    # - If S contains only '.', the function should return 0 since there are no potholes to patch.
    # - If S contains only 'X', the function should return ceil(len(S) / 3) since we can patch every three characters with one patch.
    # - If S contains a mix of 'X' and '.', the function should correctly count the number of patches needed to cover all the 'X' characters, ensuring that we do not double count patches for overlapping potholes.

    num_patches = 0
    i = 0
    while i < len(S):
        if S[i] == 'X':
            num_patches += 1
            i += 3
        else:
            i += 1
    return num_patches

@pytest.mark.parametrize("S, expected", [
    (".X..X", 2),
    ("X.XXXXX.", 3),
    ("XXXXX", 2),
    (".....", 0),
    ("X..X..X", 3),
    ("X.X.X.X.X", 3),
    ("..X.....XXXXXXX", 4),
    ("", 0),
])

def test_solution(S, expected):
    assert solution(S) == expected