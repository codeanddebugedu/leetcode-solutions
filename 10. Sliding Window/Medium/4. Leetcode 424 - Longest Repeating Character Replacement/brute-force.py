from typing import List

"""
Time complexity -> O(N^2)
N is the number of nodes

Space complexity -> O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)
        for i in range(0, n):
            hash_map = dict()
            max_freq = 0
            for j in range(i, n):
                hash_map[s[j]] = hash_map.get(s[j], 0) + 1
                max_freq = max(max_freq, hash_map[s[j]])
                changes = (j - i + 1) - max_freq
                if changes <= k:
                    max_length = max(max_length, j - i + 1)
                else:
                    break
        return max_length
