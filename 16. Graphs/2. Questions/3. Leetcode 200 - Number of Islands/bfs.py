from typing import List
from collections import deque
import copy


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Create a copy of the grid to preserve the original input
        grid_copy = copy.deepcopy(grid)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        for i in range(len(grid_copy)):
            for j in range(len(grid_copy[0])):
                if grid_copy[i][j] == "1":
                    num_islands += 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        if (
                            0 <= x < len(grid_copy)
                            and 0 <= y < len(grid_copy[0])
                            and grid_copy[x][y] == "1"
                        ):
                            grid_copy[x][y] = "2"  # mark as visited
                            for dx, dy in directions:
                                queue.append((x + dx, y + dy))

        return num_islands
