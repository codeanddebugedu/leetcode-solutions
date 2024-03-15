"""
Selection sort
Time complexity - O(n^2)
Space complexity - O(1)
"""


def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(0, n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
