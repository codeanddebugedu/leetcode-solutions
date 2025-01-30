from typing import List, Tuple


class Solution:
    def mergeList(self, arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
        n = len(arr1)
        m = len(arr2)
        i, j = 0, 0
        count = 0
        result = []

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                count += n - i  # Count inversions
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
            return lst, 0  # Return count as 0

        mid = len(lst) // 2
        first_half = lst[:mid]
        second_half = lst[mid:]

        fh, cnt1 = self.mergeSort(first_half)
        sh, cnt2 = self.mergeSort(second_half)

        merged, count = self.mergeList(fh, sh)
        return merged, cnt1 + cnt2 + count

    def inversionCount(self, arr: List[int]) -> int:
        _, count = self.mergeSort(arr)
        return count
