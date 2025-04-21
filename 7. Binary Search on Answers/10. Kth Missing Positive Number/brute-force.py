class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i in range(0, n):
            if arr[i] < k:
                k += 1
            else:
                break
        return k
