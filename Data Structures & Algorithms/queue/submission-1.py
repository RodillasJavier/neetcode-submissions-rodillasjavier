class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        """
        init an empty queue
        """
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        """
        return wether the queue is empty or not
        """
        return self.head.next is self.tail

    def append(self, value: int) -> None:
        """
        insert value at the end of the queue
        """
        new_node = ListNode(value)
        prev_node = self.tail.prev

        prev_node.next = new_node
        new_node.next = self.tail
        new_node.prev = prev_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        """
        insert value at the beginning of the queue
        """
        new_node = ListNode(value)
        next_node = self.head.next

        next_node.prev = new_node
        new_node.prev = self.head
        new_node.next = next_node
        self.head.next = new_node

    def pop(self) -> int:
        """
        remove and return the value at the end of the queue. 
        
        If the queue is empty, return -1
        """
        if self.isEmpty():
            return -1

        to_remove = self.tail.prev
        prev_node = to_remove.prev

        prev_node.next = self.tail
        to_remove.next = None
        to_remove.prev = None
        self.tail.prev = prev_node

        return to_remove.val

    def popleft(self) -> int:
        """
        remove and return the value at the beginning of the queue. 

        If the queue is empty, return -1
        """
        if self.isEmpty():
            return -1

        to_remove = self.head.next
        next_node = to_remove.next

        next_node.prev = self.head
        to_remove.next = None
        to_remove.prev = None
        self.head.next = next_node

        return to_remove.val
