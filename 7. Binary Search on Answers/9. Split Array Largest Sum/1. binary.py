from typing import List

class Solution:
    """ Function to count partitions such 
    that each partition has sum <= maxSum"""
    def countPartitions(self, nums, maxSum):
        n = len(nums)
        partitions = 0
        subarraySum = 0

        for i in range(n):
            if subarraySum + nums[i] <= maxSum:
                # Add element to the current subarray
                subarraySum += nums[i]
            else:
                # Start a new subarray with current element
                partitions += 1
                subarraySum = nums[i]
        return partitions
    
    def splitArray(self, nums: List[int], k: int) -> int:
        # Initialize binary search boundaries
        low = max(nums)  
        high = sum(nums) 

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = self.countPartitions(nums, mid)

            if partitions > k:
                """ If partitions exceed k, increase 
                the minimum possible subarray sum"""
                low = mid + 1
            else:
                """ If partitions are within k, try to 
                minimize the subarray sum further"""
                high = mid - 1

        """ After binary search, 'low' will be
        the largest minimum subarray sum with
        at most k partitions"""
        return low
