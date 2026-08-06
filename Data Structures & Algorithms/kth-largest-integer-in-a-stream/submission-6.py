import heapq


class KthLargest:
    """
    Class to find the kth largest integer in a stream of values, including
    duplicates.

    E.g. the 2nd largest from [1, 2, 3, 3] is 3.

    constraints:
        - 1 <= k <= 1000
    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Add the val to the stream and return the kth largest integer
        """
        # Case 1: The heap is full
        if len(self.heap) >= self.k:
            # the val is big enough to be in the top k

            if self.heap[0] < val:
                heapq.heapreplace(self.heap, val)
        else:
            # Case 2: The heap isn't full
            heapq.heappush(self.heap, val)

        return self.heap[0]


# time complexity: O(n log k)
# space complexity: O(k)
