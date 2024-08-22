# Using LEFT shift
class Solution:
    def checkKthBit(self, n, k):
        if n & (1 << k) != 0:
            return True
        return False


# Using RIGHT shift
class Solution:
    def checkKthBit(self, n, k):
        if (n >> k) & 1 == 1:
            return True
        return False
