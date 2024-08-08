class Solution:
    def findTwoElement(self, arr, n):
        sN = (n * (n + 1)) // 2
        s2N = (n * (n + 1) * (2 * n + 1)) // 6

        s = 0
        s2 = 0
        for num in arr:
            s += num
            s2 += num**2

        val1 = s - sN  # x-y
        val2 = s2 - s2N  # x^2 - y^2

        # This is x+y
        val2 = val2 // val1  # (x^2 - y^2)// x-y
        x = (val1 + val2) // 2
        y = x - val1

        return [x, y]
