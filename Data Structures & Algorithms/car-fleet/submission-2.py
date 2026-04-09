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

        stack = []
        for pos, spd in reversed(pairs):
            finish_time = (target - pos) / spd
            
            if not stack or finish_time > stack[-1]:
                stack.append(finish_time)

        return len(stack)