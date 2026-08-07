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
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)
        
        return heapq.heappop(nums) * -1