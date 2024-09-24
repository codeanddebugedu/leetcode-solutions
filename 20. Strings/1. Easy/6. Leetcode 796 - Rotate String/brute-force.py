class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        current_string = s
        for i in range(n):
            if current_string == goal:
                return True
            current_string = current_string[-1] + current_string[:-1]
        return False
