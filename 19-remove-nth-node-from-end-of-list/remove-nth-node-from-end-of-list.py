# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode()
        dummy.next = head
        fp = dummy
        sp = dummy
                
        for i in range(0, n):           
            fp = fp.next
       
        while fp != None and fp.next != None:            
            fp = fp.next
            sp = sp.next
        
        sp.next = sp.next.next

        return dummy.next
