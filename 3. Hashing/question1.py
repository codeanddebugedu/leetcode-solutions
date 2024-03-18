"""
Question link

https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446
"""

from typing import *


def countFrequency(n: int, m: int, edges: List[List[int]]):

    mylst = [0] * n

    for x in edges:
        if x > n:
            continue
        mylst[x - 1] += 1
    return mylst
