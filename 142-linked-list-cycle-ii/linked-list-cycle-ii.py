# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while True:

            if(fast == None or fast.next == None): return None

            fast = fast.next.next
            slow = slow.next

            if(fast == slow): break

        slow = head

        while True:
            if(slow == fast): return slow

            slow = slow.next
            fast = fast.next
            


            

        