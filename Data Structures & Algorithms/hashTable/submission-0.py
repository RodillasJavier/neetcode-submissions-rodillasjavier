class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        """
        init an empty hash table with a capacity of max(1, capacity)
        """
        self.size = 0
        self.capacity = max(1, capacity)
        self.map = []
        
        for _ in range(self.capacity):
            self.map.append(None)

    def getHash(self, key) -> int:
        """
        helper function to compute the hash values for a given key
        """
        index = key % self.capacity
        return index

    def insert(self, key: int, value: int) -> None:
        """
        insert the key-value pair into the hash table if the key DNE

        update the key-value pair in table if the key already exists
        """
        index = self.getHash(key)

        while True:
            if self.map[index] is None:
                # insert case
                self.map[index] = Pair(key, value)
                self.size += 1

                if self.size >= self.capacity // 2:
                    self.resize()

                return
            elif self.map[index].key == key:
                # update case
                self.map[index].val = value
                return
            
            # Using open addressing
            index += 1
            index = index % self.capacity


    def get(self, key: int) -> int:
        """
        return the val associated with the key

        if the key DNE => return -1
        """
        index = self.getHash(key)

        while True:
            if self.map[index] is None:
                return -1
            elif self.map[index].key == key:
                return self.map[index].val
            
            # Using open addressing
            index += 1
            index = index % self.capacity


    def remove(self, key: int) -> bool:
        """
        remove the key-value pair with the given key and return True

        if the key DNE => return False
        """
        index = self.getHash(key)

        while True:
            if self.map[index] is None:
                return False
            elif self.map[index].key == key:
                self.map[index].key = None
                self.size -= 1

                return True
            
            # Using open addressing
            index += 1
            index = index % self.capacity


    def getSize(self) -> int:
        """
        return the number of keys in the hash table
        """
        return self.size


    def getCapacity(self) -> int:
        """
        return the capacity of the hash table
        """
        return self.capacity

    def resize(self) -> None:
        """
        double the capacity of the hash table
        """
        self.capacity = self.capacity * 2
        self.size = 0

        old_map = self.map
        self.map = [None for _ in range(self.capacity)]
        for entry in old_map:
            if entry is None:
                continue
            
            self.insert(entry.key, entry.val)

