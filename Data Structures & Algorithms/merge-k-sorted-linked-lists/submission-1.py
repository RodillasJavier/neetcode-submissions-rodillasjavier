# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        in:
            - lists[]
                - len k
                - linked lists sorted ascending
        out:
            - sorted linked list merging all of them together
        constraints:
            - 0 <= k <= 1000
            - 0 <= list len <= 100
            - -1000 <= each val <= 1000
        edge cases:
            - 0 lists
        """
        if not lists:
            return None
        
        while len(lists) > 1:
            next_round = []

            for i in range(0, len(lists), 2):
                left = lists[i]

                if i + 1 < len(lists):
                    right = lists[i + 1]
                else:
                    right = None

                next_round.append(self.merge_lists(left, right))
            
            lists = next_round
        
        return lists[0]

    def merge_lists(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            
            tail = tail.next
        
        if left:
            tail.next = left
        else:
            tail.next = right
        
        return dummy.next