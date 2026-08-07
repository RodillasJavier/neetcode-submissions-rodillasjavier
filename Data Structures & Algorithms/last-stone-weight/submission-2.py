import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        in:
            - int array stones
                - stones[i] = weight of the ith stone
        out:
            - at each step choose the two heaviest stones (x and y)
                - if x == y: both stones destroyed
                - if x < y: the stone of weight y is destroyed
                    - stone y has a new weight of y - x
                - continue until 1 or 0 stone(s) left
            - return the weight of the last remaining stone or 0 if none remain
        constraints:
            - 1 <= n <= 20
            - 1 <= stones[i] <= 100
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue

            x -= y
            heapq.heappush(stones, x)

        if len(stones) == 1:
            return -stones[0]

        return 0


# time complexity: O(n log n)
# space complexity: O(1)
