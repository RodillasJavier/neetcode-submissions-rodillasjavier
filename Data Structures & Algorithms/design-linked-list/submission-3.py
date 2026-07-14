class listNode:
    def __init__(self, val):
        '''Initializes the listNode object.'''
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        '''Initializes the MyLinkedList object.'''
        self.left = listNode(0)
        self.right = listNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        '''
        Get the value of the index-th node in the linked list. If the index is 
        invalid, return -1.
        '''
        current = self.left.next
        
        i = 0
        while current and i < index:
            current = current.next
            i += 1 
        
        if current and current != self.right and i == index:
            return current.val

        return -1

    def addAtHead(self, val: int) -> None:
        '''
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked 
        list.
        '''
        prev, newNode, next = self.left, listNode(val), self.left.next
        prev.next, next.prev = newNode, newNode
        newNode.prev, newNode.next = prev, next

    def addAtTail(self, val: int) -> None:
        '''
        Append a node of value val as the last element of the linked list.
        '''
        prev, newNode, next = self.right.prev, listNode(val), self.right
        prev.next, next.prev = newNode, newNode
        newNode.prev, newNode.next = prev, next

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Add a node of value val before the index-th node in the linked list. If 
        index equals the length of the linked list, the node will be appended 
        to the end of the linked list. If index is greater than the length, the 
        node will not be inserted.
        '''
        current = self.left.next
        i = 0
        while current and i < index:
            current = current.next
            i += 1

        if current and i == index:
            prev, newNode, next = current.prev, listNode(val), current
            prev.next, next.prev = newNode, newNode
            newNode.prev, newNode.next = prev, next

    def deleteAtIndex(self, index: int) -> None:
        '''
        Delete the index-th node in the linked list, if the index is valid.
        '''
        current = self.left.next
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        
        if current and current != self.right and i == index:
            prev, next = current.prev, current.next
            prev.next, next.prev = next, prev
            current.next, current.prev = None, None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)