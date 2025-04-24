import pytest
from src.sorted_and_rotated import sorted_and_rotated_brute, sorted_and_rotated_optim

test_cases = [
    ([3, 4, 5, 1, 2], True),
    ([2, 1, 3, 4], False),
    ([1, 2, 3], True),
    ([1], True)
]

@pytest.mark.parametrize('nums, expected', test_cases)
def test_sorted_and_rotated(nums, expected):
    assert sorted_and_rotated_brute(nums) == expected
    assert sorted_and_rotated_optim(nums) == expected
    