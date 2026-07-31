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
        if not lists or len(lists) <= 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.merge_list(list1, list2))
            
            lists = merged_lists
        
        return lists[0]

    def merge_list(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
