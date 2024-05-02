from typing import List


def solve(
    i: int,
    j: int,
    a: List[List[int]],
    n: int,
    ans: List[str],
    move: str,
    vis: List[List[int]],
    di: List[int],
    dj: List[int],
):
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return
    dir = "DLRU"
    for ind in range(4):
        nexti = i + di[ind]
        nextj = j + dj[ind]
        if (
            nexti >= 0
            and nextj >= 0
            and nexti < n
            and nextj < n
            and not vis[nexti][nextj]
            and a[nexti][nextj] == 1
        ):
            vis[i][j] = 1
            solve(nexti, nextj, a, n, ans, move + dir[ind], vis, di, dj)
            vis[i][j] = 0


def ratMaze(matrix: List[List[int]]) -> List[str]:
    n = len(matrix)
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [+1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    if matrix[0][0] == 1:
        solve(0, 0, matrix, n, ans, "", vis, di, dj)
    return ans
