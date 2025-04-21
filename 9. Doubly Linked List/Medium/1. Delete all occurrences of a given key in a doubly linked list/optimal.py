class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
"""


# Definition for a node in the doubly linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# Definition for a node in the doubly linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


class Solution:
    def deleteAllOccurOfX(self, head, x):
        if head is None:
            return None

        if head.next is None and head.data == x:
            return None

        temp = head
        previous = None
        new_head = head

        while temp is not None:
            front = temp.next

            if temp.data == x:
                if previous is not None:
                    previous.next = front
                if front is not None:
                    front.prev = previous
                if temp == new_head:
                    new_head = front
            else:
                previous = temp

            temp = front

        return new_head
