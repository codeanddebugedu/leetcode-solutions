class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        result = " ".join(words)
        return result
