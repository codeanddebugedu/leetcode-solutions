from typing import List


class Solution:

    def dfs(self, row, col, index, board, word, visited):
        """Recursive DFS to match the word starting from (row, col)."""

        # If all characters are matched
        if index == len(word):
            return True

        rows, cols = len(board), len(board[0])

        # Check boundaries, visited status, and character match
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if visited[row][col]:
            return False
        if board[row][col] != word[index]:
            return False

        # Mark the current cell as visited
        visited[row][col] = True

        # Try all four directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            next_row, next_col = row + dx, col + dy
            if self.dfs(next_row, next_col, index + 1, board, word, visited):
                return True

        # Backtrack - unmark the current cell
        visited[row][col] = False

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """Check if the word exists in the board."""
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if self.dfs(row, col, 0, board, word, visited):
                    return True

        return False
