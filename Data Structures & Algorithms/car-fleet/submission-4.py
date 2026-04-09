class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        in:
            - int[] position
            - position[i] position of car i (miles)
            - int[] speed
            - speed[i] speed of car i (mph)
            - int target miles
        out:
            - num of distinct car fleets that will arrive @ dest.
        constraints:
            - car cannot pass a car ahead of it
            - n == positions.length == speed.length
            - 1 <= n <= 1000
            - 0 < target <= 1000
            - 0 < speed[i] <= 1000
            - 0 <= position[i] < target
            - vals of position are unique
        edge cases:
            - target = 1
        '''
        pairs = sorted(zip(position, speed))
        num_fleets = 0
        slowest = 0

        for pos, spd in reversed(pairs):
            finish = (target - pos) / spd

            if finish > slowest:
                num_fleets += 1
                slowest = finish

        return num_fleets

# time complexity: O(n log n)
# space complexity: O(1)