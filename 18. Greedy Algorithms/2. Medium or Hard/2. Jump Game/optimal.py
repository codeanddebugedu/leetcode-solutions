"""
Time Complexity:
The complexity is O(n), where n is the number of elements in nums. 
This is because the algorithm involves a single pass through the array.

Space Complexity:
The space complexity is O(1), as no additional space is used beyond variable storage.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False

            max_index = max(max_index, i + nums[i])

        return True
