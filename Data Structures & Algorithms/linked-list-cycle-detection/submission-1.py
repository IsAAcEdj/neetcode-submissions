# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    from collections import defaultdict
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = defaultdict(int)
        cur = head
        while cur:
            if s[cur] > 0:
                return True
            s[cur] = 1
            cur = cur.next
        return False