class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(N)
"""


def findPairs(head: Node, k: int) -> [[int]]:

    my_set = set()
    temp = head
    result = []
    while temp:
        if k - temp.data in my_set:
            result.append([k - temp.data, temp.data])
        my_set.add(temp.data)
        temp = temp.next
    return result
