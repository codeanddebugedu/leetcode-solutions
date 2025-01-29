from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for k, v in freq.items():
            if v > n // 3:
                result.append(k)
            if len(result) == 2:
                break
        return result
