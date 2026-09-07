# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        in:
            - linked list
        out:
            - return max twin sum in the LL
        constraints:
            - 2 <= n <= 100,000
            - 1 <= node.val <= 100,000
        """
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        node1, node2 = prev, slow
        while node1:
            res = max(res, node1.val + node2.val)

            node1 = node1.next
            node2 = node2.next

        return res