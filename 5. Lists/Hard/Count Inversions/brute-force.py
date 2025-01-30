class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        count = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        return count
