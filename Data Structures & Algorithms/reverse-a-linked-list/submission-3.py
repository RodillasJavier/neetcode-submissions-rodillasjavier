# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        in:
            - head of a SLL
        out:
            - reverse the SLL
            - return new head
        constraints:
            - 0 <= The length of the list <= 1000
            - -1000 <= Node.val <= 1000
        edge cases:
            - n = 0
        '''
        # BC: No head or last node
        if not head or not head.next:
            return head
        
        # Reverse the next n - 1 nodes in the list
        new_head = self.reverseList(head.next)

        # reverse the link between the head and the next node
        next_node = head.next
        next_node.next = head
        head.next = None
    
        return new_head

# time complexity: O(n)
# space complexity: O(n)
