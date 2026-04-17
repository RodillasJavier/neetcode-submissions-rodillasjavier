class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        in:
            - 0 indexed string blocks
                - blocks[i] either 'W' or 'B'
            - int k : desired num of consec. black blocks
        out:
            - min num operations to get k consecutive black blocks
        constraints:
            - recolor a white block s.t. it is now black
            - 1 <= k <= blocks.length <= 100
        '''
        min_ops = 0
        for i in range(k):
            if blocks[i] == 'W':
                min_ops += 1

        L = 0
        curr = min_ops
        for R in range(k, len(blocks)):
            if blocks[R] == 'W':
                curr += 1
            
            if blocks[L] == 'W':
                curr -= 1
            L += 1

            min_ops = min(min_ops, curr)

        return min_ops


# time complexity: O(n)
# space complexity: O(1)