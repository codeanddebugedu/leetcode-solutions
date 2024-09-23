class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            # Skip any trailing spaces
            if s[i] == " ":
                i -= 1
                continue
            # Collect the characters of the current word
            word = ""
            while i >= 0 and s[i] != " ":
                word = s[i] + word
                i -= 1
            # Add the word to the result string
            if result != "":
                result += " "
            result += word
        return result
