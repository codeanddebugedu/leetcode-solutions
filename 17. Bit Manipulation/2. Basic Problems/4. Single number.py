from typing import List


# Brute Force Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        for k in hash_map:
            if hash_map[k] == 1:
                return k


# Optimal Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            ans = ans ^ nums[i]
        return ans
