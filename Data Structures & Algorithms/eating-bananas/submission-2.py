import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, 0

        for pile in piles:
            high = max(high, pile)

        lowest = high
        while low <= high:
            mid = (low + high) // 2

            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / mid)

            if time_taken > h:
                # took too long to eat
                print(mid, time_taken)
                low = mid + 1
            else:
                # room to improve
                high = mid - 1
                lowest = min(lowest, mid)
        
        return lowest