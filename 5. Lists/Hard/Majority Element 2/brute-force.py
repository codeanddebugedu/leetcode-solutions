from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(0, n):
            if len(result) == 0 or result[0] != nums[i]:
                count = 0
                for j in range(0, n):
                    if nums[j] == nums[i]:
                        count += 1
                if count > n // 3:
                    result.append(nums[i])
            if len(result) == 2:
                break
        return result
