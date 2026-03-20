"""
# Task 5 — Count Subarrays with Arithmetic Mean Equal to S

## Problem

You are given an array `A` of N integers and an integer S. Your task is to compute how many ways one can choose a **contiguous fragment** of A that has an arithmetic mean equal to S.

The arithmetic mean (average) of a fragment is the sum of the elements of the fragment divided by its length. For example, the arithmetic mean of `[1, 4, 4, 5]` is `14/4 = 3.5`.

Write a function:

```python
def solution(A, S)
```

which returns the number of contiguous fragments of A whose arithmetic means are equal to S.

> If the result is greater than 1,000,000,000, your function should return **1,000,000,000**.

## Examples

1. Given `A = [2, 1, 3]` and `S = 2`, your function should return **3**, since the arithmetic means of fragments `[2]`, `[1, 3]` and `[2, 1, 3]` are equal to 2.
2. Given `A = [0, 4, 3, -1]` and `S = 2`, your function should return **2**, since fragments `[0, 4]` and `[4, 3, -1]` have an arithmetic mean equal to 2.
3. Given `A = [2, 1, 4]` and `S = 3`, your function should return **0**, since there exist no contiguous fragments whose arithmetic mean is equal to 3.

## Assumptions

- N is an integer within the range [1..100,000]
- S is an integer within the range [−1,000,000,000..1,000,000,000]
- Each element of array A is an integer within the range [−1,000,000,000..1,000,000,000]

## Complexity Target

- Expected time complexity: **O(N)**
- Expected space complexity: **O(N)**

"""

import pytest

def solution(A, S):
    # We can use a prefix sum array to efficiently calculate the sum of any contiguous fragment.
    # The arithmetic mean of a fragment A[i:j] is (prefix_sum[j] - prefix_sum[i]) / (j - i).
    # We want this to equal S, which means prefix_sum[j] - prefix_sum[i] = S * (j - i).
    # Rearranging gives prefix_sum[j] - S * j = prefix_sum[i] - S * i.
    # This means we are looking for pairs of indices (i, j) such that prefix_sum[j] - S * j equals prefix_sum[i] - S * i.

    from collections import defaultdict

    count = 0
    prefix_sum = 0
    seen = defaultdict(int)

    for j in range(len(A)):
        prefix_sum += A[j]
        key = prefix_sum - S * (j + 1)
        count += seen[key]
        seen[prefix_sum - S * j] += 1

        if count > 1_000_000_000:
            return 1_000_000_000

    return count    

pytest_cases = [
    ([2, 1, 3], 2, 3),
    ([0, 4, 3, -1], 2, 2),
    ([2, 1, 4], 3, 0),
    ([1, 2, 3, 4], 2.5, 2),  # [1, 2, 3] and [2, 3, 4]
    ([1, 1, 1, 1], 1, 10),  # All subarrays have mean 1
    ([1, 2, 3, 4, 5], 3, 3),  # [3],
    ([1, 2, 3, 4, 5], 4, 2),  # [4], [3, 4, 5]
    ([1, 2, 3, 4, 5], 5, 1),  # [5]
    ([1, -1, 1, -1], 0, 6),   # [1, -1], [-1, 1], [1, -1], [1, -1], [-1, 1], [-1, -1]
]
@pytest.mark.parametrize("A, S, expected", pytest_cases)
def test_solution(A, S, expected):
    assert solution(A, S) == expected