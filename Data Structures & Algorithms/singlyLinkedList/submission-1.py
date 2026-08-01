class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy = ListNode()
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        current = self.dummy.next   # first real node

        i = 0
        while current:
            if i == index:
                return current.val

            current = current.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        # Add the new node to the head position (after dummy)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

        # If the list was prev empty, assign the tail to be the new node
        if self.tail == self.dummy:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.dummy

        # Advance to just before the node to remove
        i = 0
        while i < index and current:
            current = current.next
            i += 1
        
        # Remove if in bounds
        if current and current.next:
            # removing the tail
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        current = self.dummy.next
        res = []

        while current:
            res.append(current.val)
            current = current.next
        
        return res
