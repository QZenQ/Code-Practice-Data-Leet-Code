# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tp = head
        hp = head

        while(True):
            if(not tp): return False
            tp = tp.next

            if(not hp.next or not hp.next.next): return False

            hp = hp.next.next

            if(hp == tp): return True


        