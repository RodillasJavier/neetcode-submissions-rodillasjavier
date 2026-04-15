class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        in:
            - int[] nums
            - int k 
        out:
            - true iff 2 distinct indices i & j s.t.
                - nums[i] == nums[j]
                - abs(i - j) <= k
            - false o/w
        constraints:
            - 1 <= nums.length <= 100,000
            - -1,000,000,000 <= nums[i] <= 1,000,000,000
            - 0 <= k <= 100,000
        '''
        window = set()
        
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
                
        return False

# time complexity: O(n)
# space complexity: O(n)