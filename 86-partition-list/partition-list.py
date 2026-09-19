# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        s_dummy, l_dummy = ListNode(0), ListNode(0)
        s, l = s_dummy, l_dummy

        while head:
            if(head.val < x):
                s.next = head
                s = s.next
            else:
                l.next = head
                l = l.next

            head = head.next

        s.next = l_dummy.next
        l.next = None

        return s_dummy.next

