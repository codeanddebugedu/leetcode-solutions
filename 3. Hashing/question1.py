"""
Question link

https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446
"""

from typing import List


def countFrequency(n: int, m: int, edges: List[List[int]]):

    mylst = [0] * n

    for x in edges:
        if x > n:
            continue
        mylst[x - 1] += 1
    return mylst


print(countFrequency(6, 9, [1, 3, 1, 9, 2, 7]))
