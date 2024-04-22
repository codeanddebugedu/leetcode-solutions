"""
Time complexity -> O(N^2)
N is the number of characters in s

Space complexity -> O(1)
"""

# This is a slight optimization
# But still the time complexity will be same
# Its just a small optimization


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            chars = set()
            for j in range(i, n):
                chars.add(s[j])
                if len(chars) == 3:
                    count += n - j
                    break
        return count
