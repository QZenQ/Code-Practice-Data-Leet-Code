# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        pre = dummy        
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if(l1 != None):
                total = total + l1.val
                l1 = l1.next

            if(l2 != None):
                total = total + l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            pre.next = ListNode(digit)
            pre = pre.next

        return dummy.next
        