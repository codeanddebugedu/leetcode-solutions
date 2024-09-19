"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""


def searchInLinkedList(head, k):
    current = head
    while current:
        if current.data == k:
            return 1
        current = current.next
    return 0
