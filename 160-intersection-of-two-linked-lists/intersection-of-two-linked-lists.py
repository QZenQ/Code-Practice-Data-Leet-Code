# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        Aptr = headA
        Bptr = headB

        while True:
            
            if(Aptr == Bptr): return Aptr

            Aptr = Aptr.next
            Bptr = Bptr.next

            if(Aptr == Bptr == None): return None
            
            if(Aptr == None):
                Aptr = headB
                
            if(Bptr == None):                 
                Bptr = headA
              


        return None
