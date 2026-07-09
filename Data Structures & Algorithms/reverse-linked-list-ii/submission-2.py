# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(0)
        dummy.next=head

        if left==right:
            return head
        
        
        ptrl=head
        ptrlprev=dummy

        pos=1

        while pos<left:
            ptrlprev=ptrl
            ptrl=ptrl.next
            pos+=1
        
        ptr=ptrl
        while pos<right:
            
            ptr=ptr.next
            pos+=1

        prev=ptr.next
        r=prev
        
        curr=ptrl
        
        while curr != r:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        ptrlprev.next=prev
        
        return dummy.next
        
