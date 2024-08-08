class Solution:
    def findTwoElement(self, arr, n):
        repeating, missing = -1, -1

        hash_list = [0] * (n + 1)
        for num in arr:
            hash_list[num] += 1

        for i in range(1, len(hash_list)):
            if hash_list[i] == 2:
                repeating = i
            elif hash_list[i] == 0:
                missing = i
            if repeating != -1 and missing != -1:
                return [repeating, missing]
