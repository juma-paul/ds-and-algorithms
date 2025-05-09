import pytest

from src.contains_duplicate import contains_duplicate_brute, contains_duplicate_optim

test_cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, -1, 1, 3, 3, 4, 3, 2, 4, 2, -1], True),
    ([10], False),
    ([0, 0, -10e9, 10e9], True),
]

@pytest.mark.parametrize('nums, expected', test_cases)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate_brute(nums) == expected
    assert contains_duplicate_optim(nums) == expected