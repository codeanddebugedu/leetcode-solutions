class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if head is None or head.next is None:
            return head
        temp = head
        cnt0, cnt1, cnt2 = 0, 0, 0
        while temp:
            if temp.data == 0:
                cnt0 += 1
            elif temp.data == 1:
                cnt1 += 1
            else:
                cnt2 += 1
            temp = temp.next
        temp = head
        while temp:
            if cnt0 > 0:
                temp.data = 0
                cnt0 -= 1
            elif cnt1 > 0:
                temp.data = 1
                cnt1 -= 1
            elif cnt2 > 0:
                temp.data = 2
                cnt2 -= 1
            temp = temp.next
        return head
