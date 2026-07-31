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
        
        # Keep merging lists until we have one remaining
        while len(lists) > 1:
            next_round = []

            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if i + 1 < len(lists) else None

                next_round.append(self.merge_lists(left, right))
            
            lists = next_round
        
        # Return final list (all merged together)
        return lists[0]

    def merge_lists(self, left, right):
        """
        Function to merge together two already-sorted (asc) linked lists.

        in:
            - left list node
            - right list node
        out:
            - single merged head node
        """
        dummy = ListNode()
        tail = dummy

        # Zip together the lists until one runs out
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            
            tail = tail.next
        
        # Attach the rest of whichever list is remaining
        if left:
            tail.next = left
        else:
            tail.next = right
        
        return dummy.next