"""
Time complexity -> O(2 * logN) -> O(logN)
N is number of elements in nums

Space complexity -> O(1)
"""


def count(arr: [int], n: int, target: int) -> int:
    def loweBound(arr, n, target):
        ind = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    def upperBound(arr, n, target):
        ind = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    return upperBound(arr, n, target) - loweBound(arr, n, target)
