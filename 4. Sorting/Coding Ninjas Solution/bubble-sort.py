from typing import List


def bubbleSort(arr: List[int], n: int):
    n = len(arr)
    # Traverse through all array elements in reverse order
    for i in range(n - 2, -1, -1):
        # Last i elements are already in place
        for j in range(0, i + 1):
            # Traverse the array from 0 to i
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
