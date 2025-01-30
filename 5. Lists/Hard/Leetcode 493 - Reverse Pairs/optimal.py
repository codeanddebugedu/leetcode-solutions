from typing import List, Tuple


class Solution:
    def mergeList(self, arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
        n = len(arr1)
        m = len(arr2)
        count = 0
        result = []
        j = 0
        for i in range(0, n):
            while j < m and arr1[i] > 2 * arr2[j]:
                j += 1
            count += j

        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < n:
            result.append(arr1[i])
            i += 1
        while j < m:
            result.append(arr2[j])
            j += 1

        return result, count

    def mergeSort(self, lst: List[int]) -> Tuple[List[int], int]:
        if len(lst) <= 1:
            return lst, 0

        mid = len(lst) // 2
        first_half = lst[:mid]
        second_half = lst[mid:]

        fh, cnt1 = self.mergeSort(first_half)
        sh, cnt2 = self.mergeSort(second_half)

        merged, count = self.mergeList(fh, sh)
        return merged, cnt1 + cnt2 + count

    def reversePairs(self, nums: List[int]) -> int:
        m, c = self.mergeSort(nums)
        return c
