# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = 0
        num2 = 0
        mp = 1
        while True:
            
            if(l1 != None):
                num1 = (l1.val * mp) + num1 
                l1 = l1.next

            if(l2 != None):
                num1 = (l2.val * mp) + num1 
                l2 = l2.next

            if(l1 == None and l2 == None):
                break

            mp = mp * 10

        print(num1 + num2)

        sum1 = num1 + num2

        dummy = ListNode(0)
        pre = dummy
        
        if sum1 == 0: return dummy

        while sum1 > 0:
            
            w= ListNode(sum1%10)
            pre.next = w
            pre = pre.next
            sum1 = sum1//10


 
        return dummy.next   