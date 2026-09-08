# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        in:
            - head of a LL
        out:
            - return true iff there is a cycle
            - return false o/w
        constraints:
            - 0 <= n <= 1000
            - -1000 <= node.val <= 1000
        """
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False