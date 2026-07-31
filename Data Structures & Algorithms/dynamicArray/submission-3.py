class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0

        if capacity > 0:
            self.capacity = capacity
        else:
            self.capacity = 1
        
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
