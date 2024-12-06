from typing import List


class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][col] != 0:  # Avoid overwriting original zeros
                matrix[i][col] = float("inf")
        for j in range(c):
            if matrix[row][j] != 0:  # Avoid overwriting original zeros
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
