class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        reverse_number = 0
        while num > 0:
            reverse_number = (reverse_number * 10) + num % 10
            num = num // 10
        return reverse_number == x
