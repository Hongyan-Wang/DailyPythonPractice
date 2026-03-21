"""
# Task 8 — Largest Palindromic Number

## Problem

You are given a string S which consists entirely of decimal digits. By removing digits from S and reordering the remaining digits, create a **palindromic number with the largest possible decimal value**.

You should use **at least one digit**. You may reorder the digits. A palindromic number remains the same when its digits are reversed; for instance, `"7"`, `"44"` or `"919"` are palindromic.

Any palindromic number you create should **not** have leading zeros, such as in `"0990"` or `"010"`.

Write a function:

```python
def solution(S)
```

that, given a string S of N digits, returns the string representing the palindromic number with the largest value.

## Examples

1. Given `"39878"`, your function should return `"898"`.
2. Given `"00900"`, your function should return `"9"`.
3. Given `"0000"`, your function should return `"0"`.
4. Given `"54321"`, your function should return `"5"`.

## Assumptions

- N is an integer within the range [1..100,000]
- String S is made only of digits (0–9)

## Complexity Target

Write an **efficient** algorithm for the above assumptions.

"""

import pytest

def solution(S):
    """
    Construct the largest palindromic number from digits in S.

    Key insight — greedy digit-pair selection:
      For each digit d (9 down to 0), every pair of d's contributes "d...d" around the
      palindrome's centre.  To maximise value: use as many pairs as possible, largest
      digit first.  At most one leftover digit can fill the centre (choose the largest).

    Critical leading-zero rule:
      Zeros may appear inside the palindrome but NEVER as the leading character.
      Therefore zero-pairs are only included in the left half when at least one non-zero
      pair already occupies the front.  If there are no non-zero pairs, zero pairs are
      discarded and we fall back to a single non-zero middle digit (or "0" if none exists).

    Algorithm:
      1. Count occurrences of each digit (0–9).
      2. Build the non-zero part of the left half: pairs of digits 9 down to 1.
      3. Append zero pairs to the left half only if step 2 produced a non-empty string.
      4. Find the largest digit with an odd count — this becomes the centre.
      5. Combine: left_half + centre + reverse(left_half).
      6. Edge case: if the result is empty or starts with '0', return "0".

    Time complexity:  O(N) to count; O(1) to build (only 10 distinct digits)
    Space complexity: O(1)
    """

    # Step 1 — count each digit
    count = [0] * 10
    for ch in S:
        count[int(ch)] += 1

    # Step 2 — non-zero pairs (digits 9 → 1), placed at the outer positions
    left_nonzero = []
    for d in range(9, 0, -1):
        left_nonzero.append(str(d) * (count[d] // 2))
    left_nonzero_str = ''.join(left_nonzero)

    # Step 3 — zero pairs may only follow a non-zero prefix to avoid leading zeros
    zero_pairs = count[0] // 2
    if left_nonzero_str:
        left_half_str = left_nonzero_str + '0' * zero_pairs
    else:
        left_half_str = ''  # no valid non-zero prefix; discard zero pairs

    # Step 4 — best centre digit (largest digit with an odd count)
    middle_digit = ''
    for d in range(9, -1, -1):
        if count[d] % 2 == 1:
            middle_digit = str(d)
            break

    # Step 5 — assemble the palindrome
    palindrome = left_half_str + middle_digit + left_half_str[::-1]

    # Step 6 — guard: empty result or all-zero result → return "0"
    if not palindrome or palindrome[0] == '0':
        return '0'

    return palindrome


pytest_cases = [
    # --- examples from the problem statement ---
    ("39878",  "898"),        # pairs: 8×1. centre: 9. → "8"+"9"+"8"
    ("00900",  "9"),          # no non-zero pairs; zero pairs dropped; centre: 9
    ("0000",   "0"),          # no non-zero pairs; no odd-count digit → empty → "0"
    ("54321",  "5"),          # no pairs at all; best single digit is 5

    # --- additional cases ---
    ("123321", "321123"),     # pairs: 3×1, 2×1, 1×1 → left="321", no centre
    ("0001000", "1"),         # count[1]=1 (no pair), count[0]=6; left="", centre="1"
    (
        "111222333444555666777888999000",
        "987654321090123456789",
    ),                        # each digit count=3 → 1 pair each + centre 9
                              # left="9876543210", centre="9" → 21-char palindrome
    ("1234567890", "9"),      # each digit count=1; no pairs; best centre = 9
    ("0000000000", "0"),      # 10 zeros → pairs=5, left_nonzero="", left="" → "0"
    ("9876543210", "9"),      # each digit once; no pairs; best single digit = 9
]

@pytest.mark.parametrize("S, expected", pytest_cases)
def test_solution(S, expected):
    assert solution(S) == expected