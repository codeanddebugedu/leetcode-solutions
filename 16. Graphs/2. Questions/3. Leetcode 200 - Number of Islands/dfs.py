from typing import List
import copy


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Create a copy of the grid to preserve the original input
        visited = copy.deepcopy(grid)

        def dfs(i, j):
            if (
                i < 0
                or i >= len(visited)
                or j < 0
                or j >= len(visited[0])
                or visited[i][j] != "1"
            ):
                return
            visited[i][j] = "0"  # mark as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        num_islands = 0
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)

        return num_islands
