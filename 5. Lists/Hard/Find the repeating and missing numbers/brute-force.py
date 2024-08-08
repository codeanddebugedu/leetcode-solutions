"""
Time Complexity
O(N^2), where N = size of the given array.
We are using nested loops to count occurrences of every element between 1 to N.

Space Complexity
O(1) as we are not using any extra space.
"""


class Solution:
    def findTwoElement(self, arr, n):
        repeating, missing = -1, -1

        for i in range(1, n + 1):
            count = 0
            for j in range(n):
                if arr[j] == i:
                    count += 1

            if count == 2:
                repeating = i
            elif count == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return [repeating, missing]
