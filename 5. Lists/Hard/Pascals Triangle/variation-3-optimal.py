from typing import *


def generateRow(row):
    ans = 1
    ansRow = [1]

    for col in range(1, row):
        ans *= row - col
        ans //= col
        ansRow.append(ans)
    return ansRow


def pascalTriangle(n: int) -> List[List[int]]:
    ans = []

    for row in range(1, n + 1):
        ans.append(generateRow(row))
    return ans


if __name__ == "__main__":
    n = 5
    ans = pascalTriangle(n)
    print(ans)
