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
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        second = slow.next
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        ptr1, ptr2 = head, prev
        while ptr1 and ptr2:
            tmp1, tmp2 = ptr1.next, ptr2.next

            ptr1.next = ptr2
            ptr2.next = tmp1

            ptr1, ptr2 = tmp1, tmp2