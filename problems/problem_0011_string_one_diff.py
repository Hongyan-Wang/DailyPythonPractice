"""
# Task 7 — String Differing from All by at Most One Position

## Problem

Write a function:

```python
def solution(words)
```

that, given an array `words` made of N strings, each of length K, returns a string of length K that **differs from every string in the array in at most one position**.

The returned string should consist of lowercase English letters.

If there are multiple such strings, the function can return any. If no such string exists, the function should return an **empty string**.

## Examples

1. Given `words = ["aaka", "aaka", "aaja", "aaxa", "aaba"]`, one of the correct results is `"aaба"` — note that `"b"` can be replaced by any other letter and the solution will remain correct.
2. Given `words = ["bay", "zaz", "bab"]`, the function should return `"baz"`.
3. Given `words = ["aya", "aba", "abb", "zba"]`, the function should return `"aba"`.
4. Given `words = ["zzz", "bcb", "zzc"]`, the function should return `""` (empty string).

## Assumptions

- Each string in the array `words` is of length K and consists only of lowercase English letters
- N is an integer within the range [2..100,000]
- K is an integer within the range [1..100,000]
- N × K is an integer within the range [2..1,000,000]

## Complexity Target

Write an **efficient** algorithm for the above assumptions.
"""

import pytest
def solution(words):
    # Analysis:

    # Approach:
    # 1. We can start with any string from the list (e.g., the
    #    first one) as a candidate solution.
    # 2. We check if this candidate differs from every string in the list by at
    #    most one position. If it does, we can return it immediately.
    # 3. If not, we can generate new candidate strings by changing each character
    #    of the initial candidate to every possible lowercase letter and check
    #    if any of those candidates satisfies the condition.
    # 4. If we find a valid candidate, we return it. If we exhaust all possibilities without finding a valid candidate, we return an empty string.

    # Time complexity: 
    # function is_valid runs in O(N * K) in the worst case, where we compare the candidate string to each of the N strings in the list, and each comparison takes O(K) time.
    # O(N) + O(K * 26 * N*K) = O(K^2 * N) in the worst case, where we check each of the K positions for 26 possible letters against all N words.
    # 
    # Space complexity: 
    # O(K) for the candidate string, word0 and 
    # O(N * K) for the input list of words.

    # method to optimise:
    
    def is_valid(candidate):
        for word in words:
            diff_count = sum(c1 != c2 for c1, c2 in zip(candidate, word))
            if diff_count > 1:
                return False
        return True
    K= len(words[0])
    for word in words:
        if not word or len(word) != K:
            return ""  # All words must be of the same length and non-empty
    word0 = words[0]
    if is_valid(word0):
        return word0
    for i in range(len(word0)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            candidate = word0[:i] + c + word0[i+1:]
            if is_valid(candidate):
                return candidate
    return ""

def is_valid_answer(words, result):
    if not result:
        return False
    for word in words:
        diff_count = sum(1 for c1, c2 in zip(result, word) if c1 != c2)
        if diff_count > 1:
            return False
    return True

pytest_cases = [
    (["aaka", "aaka", "aaja", "aaxa", "aaba"], True),   # multiple valid answers exist
    (["bay", "zaz", "bab"], True),                       # "baz" is one valid answer
    (["aya", "aba", "abb", "zba"], True),                # "aba" is one valid answer
    (["zzz", "bcb", "zzc"], False),                      # no valid answer exists
]

@pytest.mark.parametrize("words, has_valid_answer", pytest_cases)
def test_solution(words, has_valid_answer):
    result = solution(words)
    if has_valid_answer:
        assert is_valid_answer(words, result), f"Expected a valid answer but got {result!r}"
    else:
        assert result == "", f"Expected empty string but got {result!r}"