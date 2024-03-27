"""
Time complexity -> O(N! * N)
N is number of elements in nums

Space complexity -> O(N)
"""

ans = []
ds = []


def permutation(nums, freq):
    if len(ds) == len(nums):
        ans.append(ds.copy())
        return
    for i in range(len(nums)):
        if freq[i] == 0:
            ds.append(nums[i])
            freq[i] = 1
            permutation(nums, freq)
            freq[i] = 0
            ds.pop()


permutation([1, 2, 3], [0, 0, 0])
print(ans)
