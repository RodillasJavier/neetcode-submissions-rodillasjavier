class MinHeap:
    
    def __init__(self):
        self.heap = [None]

    def push(self, val: int) -> None:
        """
        add val to the heap
        """
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0:
            parent = i // 2

            if parent > 0 and self.heap[parent] > self.heap[i]:
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

            if (
                right < len(self.heap) and 
                self.heap[right] < self.heap[left] and 
                self.heap[right] < self.heap[i]
            ):
                # swapping with right child
                self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                i = right
            elif (self.heap[i * 2] < self.heap[i]):
                # swapping with left child
                self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                i = left
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
        if nums:
            nums.append(nums[0])
        self.heap = nums
        curr = (len(self.heap) - 1) // 2

        while curr > 0:
            i = curr

            while i * 2 < len(self.heap):
                left = i * 2
                right = left + 1

                if (
                    right < len(self.heap) and 
                    self.heap[right] < self.heap[left] and 
                    self.heap[right] < self.heap[i]
                ):
                    # swapping with right child
                    self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                    i = right
                elif (self.heap[left] < self.heap[i]):
                    # swapping with left child
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                    i = left
                else:
                    # Nodes are correctly ordered
                    break

            curr -= 1

        