"""
Time complexity -> O(N! * N)
N is number of elements in nums

Space complexity -> O(N)
"""


def permutation(nums, freq, ds, ans):
    if len(ds) == len(nums):
        ans.append(ds.copy())
        return
    for i in range(len(nums)):
        if freq[i] == 0:
            ds.append(nums[i])
            freq[i] = 1
            permutation(nums, freq, ds, ans)
            freq[i] = 0
            ds.pop()


ans = []
permutation([5, 7, 9, 1], [0, 0, 0, 0], [], ans)
print(ans)
