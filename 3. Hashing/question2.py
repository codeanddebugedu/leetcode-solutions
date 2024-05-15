"""
Question link

https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382
"""

from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    # Write your code here
    n = len(v)
    hashMap = {}
    for num in v:
        if hashMap.__contains__(num):
            hashMap[num] = 1 + hashMap[num]
        else:
            hashMap[num] = 1

    minFreq = float("inf")
    minElement = float("inf")
    maxFreq = float("-inf")
    maxElement = float("inf")

    for key, freq in hashMap.items():
        if freq > maxFreq or freq == maxFreq and key < maxElement:
            maxFreq = freq
            maxElement = key
        if freq < minFreq or freq == minFreq and key < minElement:
            minFreq = freq
            minElement = key

    return [maxElement, minElement]


a = [10, 10, 10, 9, 9, 9]
print(getFrequencies(a))
b = [1, 2, 1, 1, 3, 4]
print(getFrequencies(b))
