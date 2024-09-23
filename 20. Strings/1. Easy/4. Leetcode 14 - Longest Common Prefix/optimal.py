class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result
            result += base[i]
