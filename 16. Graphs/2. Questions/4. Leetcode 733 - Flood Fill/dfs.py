from typing import List
import copy


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # If the initial color is the same as the new color, no change is needed
        if image[sr][sc] == color:
            return image

        # Create a copy of the image to preserve the original input
        visited = copy.deepcopy(image)

        def dfs(i, j, initial_color):
            if (
                i < 0
                or i >= len(visited)
                or j < 0
                or j >= len(visited[0])
                or visited[i][j] != initial_color
            ):
                return
            visited[i][j] = color  # change to the new color
            dfs(i + 1, j, initial_color)
            dfs(i - 1, j, initial_color)
            dfs(i, j + 1, initial_color)
            dfs(i, j - 1, initial_color)

        initial_color = image[sr][sc]
        dfs(sr, sc, initial_color)

        return visited
