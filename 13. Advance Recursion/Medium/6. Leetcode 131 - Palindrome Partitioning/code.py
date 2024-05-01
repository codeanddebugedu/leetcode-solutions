from typing import List

"""
Time complexity -> O((2^n) * k *(n/2))
O(2^n) to generate every substring and O(n/2)
to check if the substring generated is a palindrome. 
O(k) is for inserting the palindromes in another data structure, 
where k  is the average length of the palindrome list.

Space Complexity -> O(k*x)
The space complexity can vary depending on the length of the answer. 
k is the average length of the list of palindromes and if we have x such list 
of palindromes in our final answer. 
The depth of the recursion tree is n, so the auxiliary space required 
is equal to the O(n).
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(substring, index):
            if index == len(s):
                result.append(substring[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    substring.append(s[index : i + 1])
                    backtrack(substring, i + 1)
                    substring.pop()

        result = []
        backtrack([], 0)
        return result
