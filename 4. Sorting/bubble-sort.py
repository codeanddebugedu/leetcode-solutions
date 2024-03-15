"""
Bubble sort
Time complexity - O(n^2) (Average and worst)
Time complexity - O(n) (Best case)
Space complexity - O(1)
"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements in reverse order
    for i in range(n - 1, 0, -1):
        # Last i elements are already in place
        for j in range(0, i):
            # Traverse the array from 0 to i
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print(arr)
