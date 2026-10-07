# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left==right:
            return head
        
        ptr=head

        while ptr.val!=right:
            
            ptr=ptr.next
            prev=ptr.next
            r=prev
        
        
        
        curr=head
        while curr != r:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        
