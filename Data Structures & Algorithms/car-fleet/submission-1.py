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
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs = sorted(pairs)

        stack = []
        for i in range(len(pairs) - 1, -1, -1):
            pos, spd = pairs[i][0], pairs[i][1]
            finish_time = (target - pos) / spd
            stack.append(finish_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)