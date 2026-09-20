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
                num2 = (l2.val * mp) + num2
                l2 = l2.next

            if(l1 == None and l2 == None):
                break

            mp = mp * 10

        print(num1)
        print(num2)

        data = str(num1)
        data = data[::-1]
        num1 = int(data)

        data = str(num2)
        data = data[::-1]
        num2 = int(data)

        
        sum1 = num1 + num2

        data = str(sum1)
        #data = data[::-1]
         
        print(sum1)
        print(data)
        dummy = ListNode(0)
        pre = dummy
        
        if sum1 == 0: return dummy
        count = 0
        while sum1 > 0:
            
            w= ListNode(int(data[count]))
            pre.next = w
            pre = pre.next
            sum1 = sum1//10
            count = count + 1


 
        return dummy.next   