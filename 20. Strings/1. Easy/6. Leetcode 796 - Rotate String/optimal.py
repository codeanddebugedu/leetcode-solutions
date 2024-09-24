class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths of s and goal are the same
        if len(s) != len(goal):
            return False

        # Concatenate s with itself
        s_double = s + s

        # Check if goal is a substring of s_double
        return goal in s_double
