"""
Merge Sort
Time Complexity: O(n log n) (Best, Average, Worst)
Space Complexity: O(n)
"""

"""
Added Parameter Reverse which will have a default value as False
"""


def merge_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half, reverse)
    right_half = merge_sort(right_half, reverse)

    # Merge the sorted halves
    if reverse:
        return mergeRev(left_half, right_half)
    else:
        return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i, j = 0, 0

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from left and right halves
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


"""
Added Function to be called if Reverse is set as True
"""


def mergeRev(left, right):
    merged = []
    i, j = 0, 0

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from left and right halves
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(f"Sorted array = {sorted_arr}")
sorted_arr = merge_sort(arr, reverse=True)
print(f"Sorted array Reversed = {sorted_arr}")
