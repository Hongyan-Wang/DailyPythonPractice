"""
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

1. Given `A = [1, 2, 0, -3]`, your function should return `">>ß=<"`.

## Assumptions

- N is an integer within the range [1..1,000]
- Each element of array A is an integer within the range [−1,000,000..1,000,000]

> In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

"""
import pytest
def solution(A):
    ### This question is straightforward. We can iterate through the array and build the string based on the conditions given.

    # Solution 1:
    #   Using string operation, we can directly build the string by checking each element in the array and appending the corresponding character to the result string.
    #   Howver, this approach can be inefficient due to string concatenation in Python, which creates a new string each time. This can lead to O(N^2) time complexity in the worst case.

    # Solution 2:
    #   Using a list to build the string and then joining it at the end is more efficient. This way, we can achieve O(N) time complexity since we are only iterating through
    #   the array once and then joining the list into a string at the end.

    # Solution 3:
    #   We can also use numpy array to vectorize the operation, which can be more efficient for large arrays. However, since the problem constraints allow for a maximum of 1,000 elements, the list approach is sufficient and simpler to implement.
    #   The time complexity for this approach is O(N) due to the single pass through the array, and the space complexity is O(N) for storing the result string.



    # Time complexity: O(N) where N is the length of the input array A.
    # Space complexity: O(N) for the output string S.

    # Corner cases:
    # - If A is empty, the function should return an empty string.
    # - If all elements in A are positive, the function should return a string of '>' characters.
    # - If all elements in A are negative, the function should return a string of '<' characters.
    # - If all elements in A are zero, the function should return a string of '=' characters.
    # - If A contains a mix of positive, negative, and zero values, the function should correctly build the string based on the conditions. 

    S=[]
    for num in A:
        if num < 0:
            S.append('<')
        elif num > 0:
            S.append('>')
        else:
            S.append('=')
    return ''.join(S)

# Test cases
@pytest.mark.parametrize("A, expected", [
    ([1, 2, 0, -3], ">>=<"),
    ([0, 0, 0], "==="),
    ([1, -1, 2, -2], "><><"),
    ([], ""),
])
def test_solution(A, expected):
    assert solution(A) == expected


