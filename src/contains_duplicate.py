from typing import List

# Brute force solution [ Time: O(n^2)| Space: O(1) ]

def contains_duplicate_brute (nums: List[int]) -> bool:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Optimized solution [ Time: O(n) | Space: O(n) ]

def contains_duplicate_optim (nums: List[int]) -> bool:
    extra_space = set()

    for i in nums:
        if i in extra_space:
            return True
        extra_space.add(i)
    return False


