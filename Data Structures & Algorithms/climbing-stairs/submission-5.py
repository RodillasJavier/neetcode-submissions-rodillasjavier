class Solution:
    def climbStairs(self, n: int) -> int:
        """
        in:
            - int n => num steps to reach the top of a staircase
        out:
            - return num distinct wys to climb to the top of the staircase
        constraints:
            - can climb w/1 or 2 steps at a time
            - 1 <= n <= 45
        """
        if n < 3:
            return n
        
        steps = [1, 2]
        i = 3
        while i <= n:
            temp = steps[1]
            steps[1] = steps[1] + steps[0]
            steps[0] = temp

            i += 1
        
        return steps[1]


# time complexity: O(n)
# space complexity: O(1)