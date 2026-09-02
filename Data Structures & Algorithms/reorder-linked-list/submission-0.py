# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        half = (l // 2) + 1
        l = 0
        cur = head
        while cur:
            l += 1
            if l == half:
                mark = cur
            if l > half:
                stack.append(cur)
            cur = cur.next
        mark.next = None
        l = 0
        cur = head
        while len(stack) > 0:
            print(cur.val)
            insert = stack.pop()
            insert.next = cur.next
            cur.next = insert
            cur = insert.next