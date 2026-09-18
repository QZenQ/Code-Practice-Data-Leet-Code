# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        buffer = ListNode(0)
        buffer.next = head

        slow = head
        fast = head

        ln = 0
        mid = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            ln = ln + 1

        mid = ln
        if(fast == None):
            print(ln)            
            ln = ln * 2
            print(ln)
        else:
            print(ln)
            ln = ln * 2 + 1
            print(ln)

            
        target =  ln - n + 1

        print(target)

        count = 0
        si = None
        if n >= mid: 
            si = slow
            count = mid

        else:
            si = buffer
            count = 0

        si = buffer
        count = 0
        while si:
            if count == target -1:
                
                si.next = si.next.next
            
            
            count = count + 1
            si = si.next

        return buffer.next
            
