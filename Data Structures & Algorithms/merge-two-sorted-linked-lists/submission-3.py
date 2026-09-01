# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        prev = ListNode(None, list1)
        dummy = prev
        while cur1 and cur2:
            if cur2.val <= cur1.val:
                trunc = cur2
                cur2 = cur2.next
                trunc.next = cur1
                prev.next = trunc
                prev = prev.next
            else:
                prev = cur1
                cur1 = cur1.next
        while cur2:
            prev.next = cur2
            cur2 = cur2.next
            prev = prev.next
        return dummy.next
