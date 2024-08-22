class Solution:
    def XORfrom1ToN(self, num):
        if num % 4 == 1:
            return 1
        elif num % 4 == 2:
            return num + 1
        elif num % 4 == 3:
            return 0
        else:
            return num

    def findXOR(self, l, r):
        return self.XORfrom1ToN(l - 1) ^ self.XORfrom1ToN(r)
