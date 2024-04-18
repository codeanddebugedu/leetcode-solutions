class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxans = 0
        for i in range(len(s)):
            set = {}
            for j in range(i, len(s)):
                if s[j] in set:
                    break
                maxans = max(maxans, j - i + 1)
                set[s[j]] = 1
        return maxans
