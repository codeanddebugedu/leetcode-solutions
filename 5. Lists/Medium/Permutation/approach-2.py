"""
Time complexity -> O(N! * N)
N is number of elements in nums

Space complexity -> O(N)
"""

ans = []


def permutation(nums, index):
    if index == len(nums):
        ans.append(nums[:])
        return
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        permutation(nums, index + 1)
        nums[index], nums[i] = nums[i], nums[index]


permutation([1, 2, 3], 0)
print(ans)
