class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        in:
            - int[] nums
            - int k 
        out:
            - total num subarrays s.t. sum = k
        constraints: 
            - 1 <= n <= 20,000
            - -1,000 <= nums[i] <= 1,000
            - k can be positive or negative
        '''
        res = 0
        current_sum = 0
        prefix_sums = { 0 : 1 }

        for num in nums:
            current_sum += num
            diff = current_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        return res


# time complexity: O(n)
# space complexity: O(n)