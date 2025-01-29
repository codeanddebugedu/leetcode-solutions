connections = [[2, 1], [1, 3], [2, 4], [3, 4], [2, 5], [4, 5]]
n = 5

matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for n1, n2 in connections:
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

print(matrix)
