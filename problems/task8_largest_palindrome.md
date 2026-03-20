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
