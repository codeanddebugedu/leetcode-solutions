"""
Time complexity -> O(N)
Space complexity -> O(1)
"""

n = 6
prev2 = 0
prev = 1
for i in range(2, n + 1):
    curr = prev2 + prev
    prev2 = prev
    prev = curr

print(prev)
