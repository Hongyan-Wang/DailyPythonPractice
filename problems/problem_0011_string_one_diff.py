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
    # Placeholder for the actual implementation
    def is_valid(candidate):
        for word in words:
            diff_count = sum(1 for c1, c2 in zip(candidate, word) if c1 != c2)
            if diff_count > 1:
                return False
        return True
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