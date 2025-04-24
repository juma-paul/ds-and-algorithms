from typing import List

# Brute force solution [ Time: O(n^2) | Space: O(n) ]

def sorted_and_rotated_brute(nums: List[int]) -> bool:
    sorted_nums = sorted(nums)

    for i in range(len(nums)):
        rotated = nums[i:] + nums[:i]
        if rotated == sorted_nums:
            return True
    return False


# Optimized solution [ Time: O(n) | Space: O(1) ]

def sorted_and_rotated_optim(nums: List[int]) -> bool:
    breaks = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            breaks += 1
    return breaks <= 1