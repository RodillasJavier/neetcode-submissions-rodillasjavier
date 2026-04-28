class Node:
    def __init__(self, key, val):    
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # map key -> node
        self.cache = {}
        self.cap = capacity

        self.LRU = Node(-1, -1)
        self.MRU = Node(-1, -1)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    # Remove a node from the DLL
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert a node at the end of the DLL
    def insert(self, node):
        prv = self.MRU.prev
        self.MRU.prev = node
        prv.next = node

        node.prev = prv
        node.next = self.MRU

    # Return the assoc. value with key
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        else:
            return -1
        
    # Insert a key val pairing into the cache
    # Removes the LRU pairing if we exceed the capacity of the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            key_to_remove = self.LRU.next.key
            self.remove(self.LRU.next)
            del self.cache[key_to_remove]


# Time complexity: O(1)
# Space complexity: O(n)