"""
Time complexity -> O(N! * N)
N is number of elements in nums

Space complexity -> O(1)
"""


def permutation(nums, index, ans):
    if index == len(nums):
        ans.append(nums.copy())
        return
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        permutation(nums, index + 1, ans)
        nums[index], nums[i] = nums[i], nums[index]


ans = []
permutation([1, 2, 3, 4], 1, ans)
print(ans)
