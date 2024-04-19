class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)
        left = 0
        right = 0
        hash_map = dict()
        max_freq = 0
        while right < n:
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_freq = max(max_freq, hash_map[s[right]])
            while right - left + 1 - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
