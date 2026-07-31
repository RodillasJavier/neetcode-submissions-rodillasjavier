class DynamicArray:
    def __init__(self, capacity: int):
        """
        init an empty array with a capacity > 0
        """
        self.size = 0

        if capacity <= 0:
            self.capacity = 1
        else:
            self.capacity = capacity
        
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        """
        return the element at index i
        """
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        """
        set the element at the index i to n
        """
        self.array[i] = n

    def pushback(self, n: int) -> None:
        """
        push the element n to the end of the array
        """
        if self.size >= self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """
        pop and return the element at the end of the array
        """
        if self.size <= 0:
            return None 

        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        """
        double the capacity of the array
        """
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array

    def getSize(self) -> int:
        """
        return the number of elements in the array
        """
        return self.size

    def getCapacity(self) -> int:
        """
        return the capacity of the array
        """
        return self.capacity
