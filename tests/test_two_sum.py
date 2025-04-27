import pytest
from src.two_sum import two_sum_brute, two_sum_optim

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([0, 150, 3], 3, [0, 2]),
    ([-10**9, 10**9], 0, [0, 1]),
]

@pytest.mark.parametrize('nums, target, expected',test_cases)
def test_two_sum(nums, target, expected):
    assert two_sum_brute(nums, target) == expected
    assert two_sum_optim(nums, target) == expected