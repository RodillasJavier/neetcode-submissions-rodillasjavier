class MinHeap:
    
    def __init__(self):
        self.heap = [None]

    def push(self, val: int) -> None:
        """
        add val to the heap
        """
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1:
            parent = i // 2

            if self.heap[parent] > self.heap[i]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def pop(self) -> int:
        """
        remove and return the smallest element in the heap. If the heap is 
        empty, return -1
        """
        result = self.top()
        if result == -1:
            return result

        i = 1
        self.heap[1] = self.heap[-1]
        self.heap.pop()
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
                # Nodes are correctly ordered
                break

        return result

    def top(self) -> int:
        """
        return the smallest element in the heap without removing it. If the 
        heap is empty, return -1
        """
        if len(self.heap) <= 1:
            return -1
        else:
            return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        """
        build a minimum heap from nums
        """
        self.heap = [None] + nums[:]
        curr = (len(self.heap) - 1) // 2

        while curr > 0:
            i = curr

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
                    # Nodes are correctly ordered
                    break

            curr -= 1

        