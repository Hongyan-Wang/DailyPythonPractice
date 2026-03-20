# Task 9 — Digit-Sum Fibonacci Sequence

## Problem

Consider the following infinite sequence:

```
0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
```

The 0th element is `0` and the 1st element is `1`. The successive elements are defined recursively — each of them is the **sum of the separate digits** of the two previous elements.

For example:
- Element 7 is `13` (regular Fibonacci), so element 8 = digits of `8` + digits of `13` = `8 + 1 + 3 = 12`
- Element 9 = digits of `13` + digits of `12` = `1 + 3 + 1 + 2 = 7`
- Element 10 = digits of `12` + digits of `7` = `1 + 2 + 7 = 10`

Write a function:

```java
class Solution { public int solution(int N); }
```

or equivalently in Python:

```python
def solution(N)
```

that, given an integer N, returns the **N-th element** of the above sequence.

## Examples

1. Given `N = 2`, the function should return `1`.
2. Given `N = 6`, the function should return `8`.
3. Given `N = 10`, the function should return `10`.

## Assumptions

- N is an integer within the range [0..1,000,000,000]

## Complexity Target

Write an **efficient** algorithm for the above assumptions.
