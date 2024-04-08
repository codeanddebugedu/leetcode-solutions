"""
Bubble sort
Time complexity - O(n^2) (Average and worst)
Time complexity - O(n) (Best case)
Space complexity - O(1)
"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements in reverse order
    for i in range(n - 2, -1, -1):
        # Last i elements are already in place
        for j in range(0, i + 1):
            # Traverse the array from 0 to i
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print(arr)

# Bubble Sort Implementation with Optimization using flag

"""
Time complexity - O(n^2) (Average and worst)
In the worst-case scenario, the list is in reverse order, 
causing both outer and inner for loop to be executed at fullest.

Time complexity - O(n) (Best case)
In the best-case scenario, the list is already sorted.
This means that during each pass through the list, there are no elements that need to be swapped
When inner for loop will run for first time, the if conditon (if arr[j] > arr[j + 1]:) will never be true
as the list is already sorted and flag 'swap' will remain False indicating no swaps were done
Hence, the inner for loop will get executed only once till 'n-1' which is nothing but first value of 'i'.
O(n-1) ~ O(n)

Space complexity - O(1)
does not require any extra space
"""


def bubble_sort1(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            # exits as there were no swaps meaning list is sorted
            return


arr = [64, 25, 12, 22, 11, 27, 0, -15]
bubble_sort1(arr)
print(arr)
