# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head

        h=set()

        while p:
            if p.next in h:
                return True
            else:
                h.add(p.next)
                p=p.next

        return False
