from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        # Initialize pointers for traversal.
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        # Traverse the matrix in a spiral order.
        while top <= bottom and left <= right:
            # Move left to right across the top row.
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Move top to bottom along the right column.
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Move right to left across the bottom row (if still valid).
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Move bottom to top along the left column (if still valid).
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
