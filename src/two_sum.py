from typing import List

# Brute Force Solution [Time: O(n^2) | Space: O(1)]

def two_sum_brute(nums: List[int], target: int) -> List[int]:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized Solution [Time: O(n) | Space: O(n)]

def two_sum_optim(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in hashmap:
            return [hashmap[complement], index]
        hashmap[value] = index
    