class DynamicArray:
    
    def __init__(self, capacity: int):
        """
        init an empty array with a capacity > 0
        """
        self.array = []

        if capacity <= 0:
            self.capacity = 1
        else:
            self.capacity = capacity

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
        if len(self.array) >= self.capacity:
            self.resize()
            
        self.array.append(n)


    def popback(self) -> int:
        """
        pop and return the element at the end of the array
        """
        return self.array.pop()
 

    def resize(self) -> None:
        """
        double the capacity of the array
        """
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        """
        return the number of elements in the array
        """
        return len(self.array)
    
    def getCapacity(self) -> int:
        """
        return the capacity of the array
        """
        return self.capacity
