from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        for i in range(0, n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                maxi = max(maxi, product)
        return maxi
