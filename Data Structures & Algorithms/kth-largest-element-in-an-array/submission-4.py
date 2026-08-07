import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        in:
            - unsorted int array nums
            - int k 
        out:
            - return the kth largest element in the sorted order
        constraints:
            - do without sorting
            - 1 <= k <= n <= 10,000
            - nums[i] can be pos or neg
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
