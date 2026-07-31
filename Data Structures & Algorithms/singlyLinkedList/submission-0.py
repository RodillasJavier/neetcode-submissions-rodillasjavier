class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next

        i = 0
        while current:
            if i == index:
                return current.val

            current = current.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.head

        i = 0
        while i < index and current:
            current = current.next
            i += 1
        
        if current and current.next:
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        res = []

        while current:
            res.append(current.val)
            current = current.next
        
        return res
