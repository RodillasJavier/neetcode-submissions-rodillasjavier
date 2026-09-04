# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        in:
            - head of a SLL
        out:
            - return the middle node of the LL
            - if two mid nodes, return the right one
        constraints:
            - 1 <= n <= 100
            - 1 <= node.val <= 100
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow