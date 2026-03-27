"""
## Problem

You have M square tiles of size 1×1 and N square tiles of size 2×2. Your task is to create the **largest possible square** using these tiles. Tiles may not overlap, and the resulting square should be filled completely (it should not contain empty spaces).

Write a function:

```python
def solution(M, N)
```

that, given two integers M and N, returns the **length of the side** of the largest square you can create. If no square can be created, your function should return 0.

## Examples

1. Given `M = 8` and `N = 0`, your function should return **2**. You can use four out of eight 1×1 tiles to arrange them into a 2×2 square. There are not enough tiles to create a 3×3 square.

2. Given `M = 4` and `N = 3`, your function should return **4**. You can obtain a 4×4 square by arranging four 1×1 tiles into a 2×2 area in the centre, and surrounding it with 2×2 tiles:

   ```
   [2x2][2x2]
   [2x2][1x1 1x1]
        [1x1 1x1]
   ```

3. Given `M = 0` and `N = 18`, your function should return **8**. You need to use sixteen 2×2 tiles to create an 8×8 square. Note that not all tiles need to be used.

4. Given `M = 13` and `N = 3`, your function should return **5**. One of the possible arrangements uses the 2×2 tiles to fill part of the 5×5 area, and 1×1 tiles fill the remainder.

## Assumptions

- M and N are integers within the range [0..1,000,000,000]

## Complexity Target

Write an **efficient** algorithm for the above assumptions.
"""


import pytest
import math 
def solution1(M, N):
    # Analysis:

    # Approach:
    # 1. The largest square we can create will have a side length of at most `2 * N + 1`, since we can use at most N 2×2 tiles and one 1×1 tile to fill the center if needed.
    # 2. We can iterate from the largest possible side length down to 1, checking if we can create a square of that size using the available tiles.
    # 3. For each candidate side length `s`, we calculate how many 2×2 tiles and 1×1 tiles are needed to fill a square of that size.
    # 4. If the required number of tiles is less than or equal to the available tiles (M and N), we return that side length as the answer.

    # Time complexity: O(s) where s is the largest possible side length, which is O(N).
    # Space complexity: O(1) since we only use a constant amount of space for calculations.
    def is_valid(M, N, s):
        # Calculate the number of 2x2 tiles needed
        N_used = min(N, (s // 2) ** 2)
        # Calculate the number of 1x1 tiles needed
        M_needed = s * s - N_used * 4
        return M_needed <= M
    
    max_side = int(math.sqrt(M + 4 * N))+ 1  # Maximum possible side length based on available tiles   
    min_side = 0
    while min_side < max_side:
        mid_side = (min_side + max_side + 1) // 2
        if is_valid(M, N, mid_side):
            min_side = mid_side
        else:
            max_side = mid_side - 1
    return min_side 
# what did solution 1 miss? 
# --- I did not consider the case where if only N then s can only be even 
# BUT THE binary search go with each length gradually. 

def solution2(M, N):
    # A more straightforward approach without binary search, but less efficient for large N.
    def is_valid(M, N, s):
        N_used = min(N, (s // 2) ** 2)
        M_needed = s * s - N_used * 4
        return M_needed <= M
    if M == 0 and N == 0:
        return 0
    # if s is even 
    max_side = int(math.sqrt(M + 4 * N)) + 1
    mini_side = 0
    low, high = 0, max_side//2 # half length
    while low < high:
        mid = (low + high+1) // 2
        if is_valid(M, N, 2*mid):
            low = mid
        else:
            high = mid - 1
    mini_side_even = 2*low

    # if s is odd
    low, high = 0, (max_side)//2+1 # half length
    while low < high:
        mid = (low + high+1) // 2
        if is_valid(M, N, 2*mid+1):
            low = mid 
        else:
            high = mid-1
    mini_side_odd = 2*low + 1   
    return max(mini_side_even, mini_side_odd)  

def solution3(M, N):
    if M == 0 and N == 0:
        return 0
    def can_build_even(M, N, k):
        s = 2 * k
        N_used = min(N, k * k)
        M_needed = s * s - N_used * 4
        return M_needed <= M

    def can_build_odd(M, N, k):
        s = 2 * k + 1
        N_used = min(N, k * k)
        M_needed = s * s - N_used * 4
        return M_needed <= M

    # Binary search for the largest k such that check_fn(k) is true
    def binary_search_max(upper_bound, check_fn):
        left, right = 0, upper_bound
        while left < right:
            mid = (left + right + 1) // 2
            if check_fn(M, N, mid):
                left = mid
            else:
                right = mid - 1
        return left

    max_side = int(math.sqrt((M + 4 * N))) + 1
    best_even_k = binary_search_max(max_side // 2, can_build_even)
    best_odd_k = binary_search_max(max_side // 2, can_build_odd)

    best_even_side = 2 * best_even_k
    best_odd_side = 2 * best_odd_k + 1 

    return max(best_even_side, best_odd_side)


all_solutions = [
    #solution1,
    solution2,  # add new solutions here
    solution3,
]

pytest_cases = [
    (8, 0, 2),
    (4, 3, 4),
    (0, 18, 8),
    (13, 3, 5),
    (0, 0, 0),  # No tiles available
    (1, 0, 1),  # Only one 1x1 tile
    (0, 1, 2),  # Only one 2x2 tile
    (5, 1, 3),  # Enough for a 3x3
    (10, 2, 4), # Enough for a 4x4
]

@pytest.mark.parametrize("solution", all_solutions, ids=lambda f: f.__name__)
@pytest.mark.parametrize("M, N, expected", pytest_cases)
def test_solution(M, N, expected, solution):
    assert solution(M, N) == expected, f"Expected {expected} but got {solution(M, N)} for M={M}, N={N}" 

