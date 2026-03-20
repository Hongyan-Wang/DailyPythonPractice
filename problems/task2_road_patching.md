# Task 2 — Road Patching

## Problem

There is a road consisting of N segments, numbered from 0 to N-1, represented by a string `S`. Segment `S[K]` may contain a pothole, denoted by a single uppercase `"X"`, or may be a good segment without any potholes, denoted by a single dot `"."`.

The road fixing machine can patch over **three consecutive segments** at once with asphalt and repair all the potholes located within each of those three segments. Good or already repaired segments remain good after patching them.

Your task is to compute the **minimum number of patches** required to repair all the potholes in the road.

Write a function:

```python
def solution(S)
```

that, given a string `S` of length N, returns the minimum number of patches required to repair all the potholes.

## Examples

1. Given `S = ".X..X"`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 2-4.
2. Given `S = "X.XXXXX."`, your function should return **3**. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
3. Given `S = "XX.XXX.."`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 3-5.
4. Given `S = "XXXX"`, your function should return **2**. The road fixing machine could patch, for example, segments 0-2 and 1-3.

## Assumptions

- N is an integer within the range [3..100,000]
- String S consists only of the characters `"."` and `"X"`
