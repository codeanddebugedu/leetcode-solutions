class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, w, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= w:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = w - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue
