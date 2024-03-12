"""
Check if a string is palindrome
using recursion
"""


def checkPalindrome(string, i):
    if i >= len(string) // 2:
        return True
    if string[i] != string[len(string) - i - 1]:
        return False
    return checkPalindrome(string, i + 1)


if __name__ == "__main__":
    result = checkPalindrome("momm", 0)
    print(result)
