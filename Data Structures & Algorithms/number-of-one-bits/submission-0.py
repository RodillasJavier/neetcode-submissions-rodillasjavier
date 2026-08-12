class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        in:
            - unsigned integer n
        out:
            - return the num of 1 bits in its bin representation
        constraints:
            - n is non-negative
        """
        result = 0

        while n > 0:
            if n & 1:
                result += 1
            
            n = n >> 1
        
        return result