class MinHeap:
    
    def __init__(self):
        self.heap = [None]

    def push(self, val: int) -> None:
        """
        add val to the heap
        """
        print(f"pushing {val} onto {self.heap}")
        self.heap.append(val)

        i = len(self.heap) - 1
        while i > 1:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2
            else:
                break

    def pop(self) -> int:
        """
        remove and return the smallest element in the heap. If the heap is 
        empty, return -1
        """
        if len(self.heap) == 1:
            return -1
        result = self.heap[1]

        self.heap[1] = self.heap[-1]
        self.heap.pop()

        i = 1
        while i * 2 < len(self.heap):
            left = i * 2
            right = left + 1

            smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right
            
            if self.heap[smallest] < self.heap[i]:
                self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                i = smallest
            else:
                break

        return result


    def top(self) -> int:
        """
        return the smallest element in the heap without removing it. If the 
        heap is empty, return -1
        """
        if len(self.heap) == 1:
            return -1
        
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        """
        build a minimum heap from nums
        """
        self.heap = [None] + nums

        current = (len(self.heap) - 1) // 2
        while current > 0:
            i = current

            while i * 2 < len(self.heap):
                left = i * 2
                right = left + 1

                smallest = left
                if right < len(self.heap) and self.heap[right] < self.heap[left]:
                    smallest = right
                
                if self.heap[smallest] < self.heap[i]:
                    self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                    i = smallest
                else:
                    break
            
            current -= 1



        