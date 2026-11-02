# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode()
        dummy2 = ListNode()

        dummy1.next = head

        pre = dummy1 
        minN = dummy2

        while(pre!=None and pre.next != None):

            if(pre.next.val < x):
                minN.next = pre.next
                minN = minN.next

                pre.next = pre.next.next
            else:
                pre = pre.next 

            

        minN.next = dummy1.next

        return dummy2.next