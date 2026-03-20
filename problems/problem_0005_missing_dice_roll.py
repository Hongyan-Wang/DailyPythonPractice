"""
# Task 3 — Missing Dice Rolls

## Problem

You have just rolled a dice several times. The N roll results that you remember are described by an array `A`. However, there are F rolls whose results you have forgotten. The arithmetic mean of **all** the roll results (the sum of all the roll results divided by the number of rolls) equals M.

**What are the possible results of the missing rolls?**

Write a function:

```python
def solution(A, F, M)
```

that, given an array `A` of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. The returned array should contain F integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return `[0]`.

## Examples

1. Given `A = [3, 2, 4, 3]`, `F = 2`, `M = 4`, your function should return `[6, 6]`. The arithmetic mean of all the rolls is `(3 + 2 + 4 + 3 + 6 + 6) / 6 = 24 / 6 = 4`.
2. Given `A = [1, 5, 6]`, `F = 4`, `M = 3`, your function may return `[2, 1, 2, 4]` or `[6, 1, 1, 1]` (among others).
3. Given `A = [1, 2, 3, 4]`, `F = 4`, `M = 6`, your function should return `[0]`. It is not possible to obtain such a mean.
4. Given `A = [6, 1]`, `F = 1`, `M = 1`, your function should return `[0]`. It is not possible to obtain such a mean.

## Assumptions

- N and F are integers within the range [1..100,000]
- Each element of array A is an integer within the range [1..6]
- M is an integer within the range [1..6]

> Remember, all submissions are being checked for plagiarism. Your recruiter will be informed in case suspicious activity is detected.

"""

import pytest

def solution(A, F, M):
    # Approach: check corner cases and then calculate the missing rolls based on the required total sum

    # time complexity: O(N) to calculate the sum of known rolls, and O(F) to construct the result array
    # space complexity: O(F) for the result array
    total_rolls = len(A) + F
    known_sum = sum(A)
    total_sum_needed = M * total_rolls
    missing_sum_needed = total_sum_needed - known_sum

    # Check if it's possible to achieve the desired average with the missing dice rolls
    if missing_sum_needed < F or missing_sum_needed > 6 * F:
        return [0]
    base = missing_sum_needed // F
    remainder = missing_sum_needed % F
    possible_rolls = [base + 1] * remainder + [base] * (F - remainder)
    return possible_rolls   

def is_valid_solution(A, F, M, result):
    if len(result) != F:
        return False
    if any(roll < 1 or roll > 6 for roll in result):
        return False
    total_sum = sum(A) + sum(result)
    return total_sum == M * (len(A) + F)

@pytest.mark.parametrize("A, F, M, possible", [
    ([3, 2, 4, 3], 2, 4, True),
    ([1, 5, 6], 4, 3, True),
    ([1, 2, 3, 4], 4, 6, False),
    ([6, 1], 1, 1, False),
    ([3], 3, 5, True)
])
def test_solution(A, F, M, possible):
    result = solution(A, F, M)
    if possible:
        assert result != [0] and is_valid_solution(A, F, M, result)
    else:
        assert result == [0]