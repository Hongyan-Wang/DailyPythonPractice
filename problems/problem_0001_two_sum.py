import pytest


def two_sum_solution(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ],
)
def test_two_sum_solution(inputs, expected):
    assert two_sum_solution(*inputs) == expected