"""
Time complexity -> O(N)
N is the number of brackets

Space complexity -> O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if (
                    (bracket == ")" and ch == "(")
                    or (bracket == "]" and ch == "[")
                    or (bracket == "}" and ch == "{")
                ):
                    continue
                else:
                    return False
        return len(stack) == 0
