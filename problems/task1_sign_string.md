# Task 1 — Sign String

## Problem

Write a function:

```python
def solution(A)
```

that, given an array `A` of N integers, returns a string `S` as follows:

- `S[J]` is set to `'<'` if `A[J] < 0`
- `S[J]` is set to `'>'` if `A[J] > 0`
- `S[J]` is set to `'='` if `A[J] = 0`

`S` should not contain any characters other than `'<'`, `'>'` and `'='`.

## Examples

1. Given `A = [1, 2, 0, -3]`, your function should return `">>=<"`.

## Assumptions

- N is an integer within the range [1..1,000]
- Each element of array A is an integer within the range [−1,000,000..1,000,000]

> In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.
