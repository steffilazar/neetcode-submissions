# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=head

        h=set()

        while head.next!=None:
            if head.next in h:
                return True
            else:
                h.add(head.next)
                head=head.next

        return False
