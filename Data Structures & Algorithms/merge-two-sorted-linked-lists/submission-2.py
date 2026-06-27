# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        in:
            - heads of 2 sorted LL
        out:
            - merge the two lists into one
            - return head of new sorted list
        '''
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next
        
        if not list1:
            dummy.next = list2
        else:
            dummy.next = list1
        
        return head.next