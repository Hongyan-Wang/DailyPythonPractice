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
    """
    Count contiguous subarrays of A whose arithmetic mean equals S.

    Key insight — transform to zero-sum subarray counting:
      Define B[k] = A[k] - S.
      A subarray A[i..j] has mean S  iff  sum(A[i..j]) = S*(j-i+1)
                                      iff  sum(B[i..j]) = 0.

    Using prefix sums of B (prefix_B[k] = B[0]+...+B[k-1], with prefix_B[0] = 0):
      sum(B[i..j]) = 0  iff  prefix_B[j+1] = prefix_B[i].

    So the answer is the number of index pairs (i, j) with 0 ≤ i < j ≤ N
    where prefix_B[i] = prefix_B[j].  A hash map lets us count these in O(N).

    Time complexity:  O(N)
    Space complexity: O(N)
    """

    count = 0
    A_minus_S = []                # Running prefix sum of B; starts at prefix_B[0] = 0
    current_sum = 0
    current_sum_dict ={}
    for a in A:
        A_minus_S.append(a - S) 
        current_sum += A_minus_S[-1]  
        if current_sum == 0:
            count += 1          
        if current_sum in current_sum_dict: 
            count += current_sum_dict[current_sum]
            current_sum_dict[current_sum] += 1
        else:
            current_sum_dict[current_sum] = 1
        if count > 1_000_000_000:
            return 1_000_000_000

    return count


pytest_cases = [
    ([2, 1, 3], 2, 3),              # [2], [1,3], [2,1,3]
    ([0, 4, 3, -1], 2, 2),          # [0,4], [4,3,-1]
    ([2, 1, 4], 3, 0),              # no valid subarrays
    ([1, 2, 3, 4], 2.5, 2),         # [2,3], [1,2,3,4]
    ([1, 1, 1, 1], 1, 10),          # every subarray has mean 1 → C(5,2) = 10 pairs
    ([1, 2, 3, 4, 5], 3, 3),        # [3], [2,3,4], [1,2,3,4,5]
    ([1, 2, 3, 4, 5], 4, 2),        # [4], [3,4,5]
    ([1, 2, 3, 4, 5], 5, 1),        # [5]
    ([1, -1, 1, -1], 0, 4),         # [1,-1](0-1), [-1,1](1-2), [1,-1](2-3), [1,-1,1,-1](0-3)
]
@pytest.mark.parametrize("A, S, expected", pytest_cases)
def test_solution(A, S, expected):
    assert solution(A, S) == expected