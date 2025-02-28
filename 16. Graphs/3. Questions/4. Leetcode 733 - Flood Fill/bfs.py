from typing import List
from collections import deque
import copy


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # If the initial color is the same as the new color, no change is needed
        if image[sr][sc] == color:
            return image

        visited = copy.deepcopy(image)
        initial_color = image[sr][sc]
        queue = deque([(sr, sc)])

        while queue:
            x, y = queue.popleft()
            if visited[x][y] == initial_color:
                visited[x][y] = color
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < len(visited)
                        and 0 <= ny < len(visited[0])
                        and visited[nx][ny] == initial_color
                    ):
                        queue.append((nx, ny))

        return visited
