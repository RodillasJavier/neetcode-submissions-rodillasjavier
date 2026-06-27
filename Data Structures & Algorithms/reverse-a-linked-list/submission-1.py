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
        current = head
        prev = None
        while current != None:
            nxt = current.next
            current.next = prev

            prev = current
            current = nxt
        
        return prev

# time complexity: O(n)
# space complexity: O(1)