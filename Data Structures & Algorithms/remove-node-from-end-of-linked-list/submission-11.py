# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        dummy = head
        for i in range(n):
            r = r.next
        while r:
            print("it")
            r = r.next
            dummy = l
            l = l.next
        if l == head and n == 1 and r:
            l.next = None
            return l
        elif l == head:
            return head.next
        else:
            dummy.next = l.next
        return head