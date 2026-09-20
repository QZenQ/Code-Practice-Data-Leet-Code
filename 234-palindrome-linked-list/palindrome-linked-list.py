# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        stack = []

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        if(dummy.next.next == None): return True
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next

            stack.append(slow.val)

        if fast != None :
            slow = slow.next
        

        for i in range(len(stack)):
            if(slow == None): return False
            data = stack.pop()
            print(slow.val)
            print(data)
            if(slow.val != data):
                return False

            slow = slow.next

        return True


            