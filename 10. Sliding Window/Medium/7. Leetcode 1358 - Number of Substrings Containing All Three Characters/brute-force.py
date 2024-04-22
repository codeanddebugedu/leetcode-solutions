"""
Time complexity -> O(N^2)
N is the number of characters in s

Space complexity -> O(1)
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            chars = set()
            for j in range(i, n):
                chars.add(s[j])
                if len(chars) == 3:
                    count += 1
        return count
