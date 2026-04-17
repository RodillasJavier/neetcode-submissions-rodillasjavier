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
        res = 0
        for i in range(k):
            if blocks[i] == 'W':
                res += 1
        # print(res)

        L = 0
        curr = res
        for R in range(k, len(blocks)):
            if blocks[R] == 'W':
                curr += 1
            
            if blocks[L] == 'W':
                curr -= 1
            L += 1

            res = min(res, curr)
            # print(blocks[L : R + 1], curr)

        return res



'''
Input: blocks = "WBBWWBBWBW", k = 7
WBBWWBBWBW
L23456R000  nw = 3
0L23456R00  nw = 3
00L23456R0  nw = 3
000L23456R  nw = 3

Input: blocks = "BWWWBB", k = 6
BWWWBB
L2345R nw = 3
'''