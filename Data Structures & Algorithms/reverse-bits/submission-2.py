class Solution:
    def reverseBits(self, n: int) -> int:
        """
        in:
            - 32bit int
        out:
            - reverse the bits of the bin rep of n
            - return the result as an integer
        """
        res = 0

        for i in range(32):
            bit = n % 2
            n = n >> 1

            res += bit
                        
            if i != 31:
                res = res << 1

        return res


# time complexity: O(1)
# space complexity: O(1)
