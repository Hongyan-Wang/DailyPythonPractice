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
