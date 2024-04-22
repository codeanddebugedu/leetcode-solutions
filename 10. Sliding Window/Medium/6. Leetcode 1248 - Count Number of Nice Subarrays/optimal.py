from typing import List

"""
Time complexity -> O(2 * 2N)
N is the number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0:
            return 0
        count = 0
        n = len(nums)
        left = 0
        right = 0
        Sum = 0
        while right < n:
            Sum += nums[right] % 2
            while Sum > goal:
                Sum -= nums[left] % 2
                left += 1
            count = count + ((right - left) + 1)
            right += 1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.countSubArrayLessThanOrEqualToGoal(
            nums, k
        ) - self.countSubArrayLessThanOrEqualToGoal(nums, k - 1)
