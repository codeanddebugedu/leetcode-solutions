"""
Time Complexity -> O(n log n)
Time Complexity -> O(n^2) (Worst Case)
Space Complexity -> O(1)
"""


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)


arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array = {arr}")
