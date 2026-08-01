class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        """
        init an empty linked list
        """
        self.dummy = ListNode()
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        """
        return the val of the ith node. If OOB, return -1
        """
        current = self.dummy.next

        i = 0
        while current:
            if i == index:
                return current.val

            i += 1
            current = current.next
        
        return -1

    def insertHead(self, val: int) -> None:
        """
        insert a node with val at the head of the LL
        """
        new_node = ListNode(val)

        new_node.next = self.dummy.next
        self.dummy.next = new_node

        if self.tail == self.dummy:
            self.tail = new_node
    

    def insertTail(self, val: int) -> None:
        """
        insert a node with val at the tail of the LL
        """
        new_node = ListNode(val)

        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        """
        remove the ith node from the LL and return True. Iff OOB, return False 
        and do nothing. 
        """
        current = self.dummy

        # Advance to just before the node to remove
        i = 0
        while current and i < index:
            i += 1
            current = current.next
        
        if current and current.next:
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next

            return True
        
        return False

    def getValues(self) -> List[int]:
        """
        return an array of all the values in the LL
        """
        current = self.dummy.next

        res = []
        while current:
            res.append(current.val)
            current = current.next
        
        return res