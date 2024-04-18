class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = dict()
        left = 0
        right = 0
        length = 0
        n = len(s)
        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]] + 1, left)
            hash_map[s[right]] = right
            length = max(length, right - left + 1)
            right += 1
        return length
