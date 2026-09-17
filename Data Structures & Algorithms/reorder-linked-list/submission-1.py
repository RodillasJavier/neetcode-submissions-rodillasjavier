# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        in:
            - head of a sll
        out: 
            - Reorder the linked list such that the last and first nodes 
                alternate in order (1 - 2 - 3 => 1 - 3 - 2)
        constraints:
            - 1 <= n <= 1000
            - 1 <= node.val <= 1000
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        left, right = head, prev
        while left and right:
            tmp1, tmp2 = left.next, right.next

            left.next = right
            right.next = tmp1

            left, right = tmp1, tmp2