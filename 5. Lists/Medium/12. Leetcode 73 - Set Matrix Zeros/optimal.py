from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        col0 = 1
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        for j in range(c - 1, 0, -1):
            if matrix[0][0] == 0:
                matrix[0][j] = 0
        for i in range(0, r):
            if col0 == 0:
                matrix[i][0] = 0
