# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        i,j =0,0

        while p:
            j+=1
            p=p.next

        p=head

        if n==j:
            return head.next
        

        while head:
            i+=1
            
            if i==j-n:
                
                head.next=head.next.next
               
            head=head.next
        return p

