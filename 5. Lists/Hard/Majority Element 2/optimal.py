from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0
        for i in range(0, n):
            if cnt1 == 0 and nums[i] != cand2:
                cnt1 = 1
                cand1 = nums[i]
            elif cnt2 == 0 and nums[i] != cand1:
                cnt2 = 1
                cand2 = nums[i]
            elif cand1 == nums[i]:
                cnt1 += 1
            elif cand2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for i in range(0, n):
            if nums[i] == cand1:
                cnt1 += 1
            if nums[i] == cand2:
                cnt2 += 1
        result = []
        if cnt1 > n // 3:
            result.append(cand1)
        if cnt2 > n // 3:
            result.append(cand2)
        return result
