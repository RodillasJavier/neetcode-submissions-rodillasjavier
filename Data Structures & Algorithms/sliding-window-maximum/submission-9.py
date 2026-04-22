from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        in:
            - int[] nums
            - int k
        out:
            - list containing max ele in window @ each step as sliding window moves
        constraints:
            - 1 <= len(nums) <= 100,000
            -10,000 <= nums[i] <= 10,000
            - 1 <= k <= nums.length
        edge cases:
            - k == 1
            - k == nums.length
        '''
        q = deque()
        res = []
        L, R = 0, 0

        # Move window thru nums
        while R < len(nums):
            # Pop off all nums smaller than R before adding to deque
            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            # Make sure that the deque only includes el in window
            if q[0] < L:
                q.popleft()

            # Only update res & L once window is size k 
            if R >= k - 1:
                res.append(nums[q[0]])
                L += 1
            
            R += 1

        return res


# time complexity: O(n)
# space complexity: O(k)