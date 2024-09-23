class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def reverse(self, head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def addOne(self, head):
        new_head = self.reverse(head)
        temp = new_head
        carry = 0
        while temp:
            if temp.data == 9:
                carry = 1
                temp.data = 0
            else:
                temp.data = temp.data + 1
                break
            if temp.next is None:
                if carry == 1:
                    temp.next = Node(1)
                    break
            temp = temp.next
        return self.reverse(new_head)
