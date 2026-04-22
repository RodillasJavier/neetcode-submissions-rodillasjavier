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
        L, R = 0, 0
        res = []

        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            if L > q[0]:
                q.popleft()

            if R + 1 >= k:
                res.append(nums[q[0]])
                L += 1

            R += 1

        return res


'''
1 2 1 0 4 2 6 | k = 3
q = [6]
res = [2 2 4 4 6]
'''
