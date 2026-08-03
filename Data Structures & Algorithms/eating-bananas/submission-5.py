import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        lowest = high

        while low <= high:
            mid = (low + high) // 2

            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / mid)

            if time_taken > h:
                # took too long to eat => search higher rates
                low = mid + 1
            else:
                # potential candidate => search slower rates
                high = mid - 1
                lowest = min(lowest, mid)

        return lowest


# time complexity: O(n log k)
# space complexity: O(1)
