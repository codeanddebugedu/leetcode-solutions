"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(N)
The code uses a hashmap/dictionary/set to store encountered nodes, 
which can take up to O(N) additional space, 
where 'n' is the number of nodes in the list.
"""


class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    my_dict = dict()
    temp = head
    travel = 0
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        my_dict[temp] = travel
        travel += 1
        temp = temp.next
    return 0
