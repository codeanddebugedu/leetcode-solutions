def func(subset: list, index: int):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    func(subset, index + 1)
    subset.pop()
    func(subset, index + 1)


result = []
nums = [45, 73, 11, 91]
func([], 0)
print(result)
