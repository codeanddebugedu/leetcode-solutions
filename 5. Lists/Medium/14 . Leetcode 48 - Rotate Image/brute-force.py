from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        result = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                result[j][r - 1 - i] = matrix[i][j]
        matrix[:] = result
