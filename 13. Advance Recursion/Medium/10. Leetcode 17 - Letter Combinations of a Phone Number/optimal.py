class Solution:
    def __init__(self):
        self.digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def helper(self, digits, ans, index, current):
        if index == len(digits):
            ans.append(current)
            return

        letters = self.digits_to_letters.get(digits[index], "")
        for letter in letters:
            self.helper(digits, ans, index + 1, current + letter)

    def letterCombinations(self, digits):
        ans = []
        if not digits:
            return ans
        self.helper(digits, ans, 0, "")
        return ans
