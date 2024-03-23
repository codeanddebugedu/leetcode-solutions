from typing import List

"""
Time complexity -> O(2n) -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = dict()
        n = len(nums)
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for k, v in hash_map.items():
            if v > n // 2:
                return k
