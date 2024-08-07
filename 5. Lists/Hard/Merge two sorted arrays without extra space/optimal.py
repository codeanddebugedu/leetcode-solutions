class Solution:
    def merge(self, arr1, arr2, n, m):
        left = n - 1
        right = 0

        while left >= 0 and right < m:
            if arr1[left] > arr2[right]:
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1
            else:
                break

        arr1.sort()
        arr2.sort()
