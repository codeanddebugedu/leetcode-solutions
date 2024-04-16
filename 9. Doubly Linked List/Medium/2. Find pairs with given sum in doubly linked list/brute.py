class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N^2)
N is the number of nodes

Space complexity -> O(1)
"""


def findPairs(head: Node, k: int) -> [[int]]:
    temp1 = head
    result = []
    while temp1.next is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.data + temp2.data == k:
                result.append([temp1.data, temp2.data])
            temp2 = temp2.next
        temp1 = temp1.next
    return result
