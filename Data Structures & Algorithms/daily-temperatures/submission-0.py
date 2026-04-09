class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        in:
            - int[] temperatures
            - temperatures[i] = daily temperatures on day i 
        out:
            - int[] result
            - result[i] = num days until the temp is greater than on day i
            - iff day i is the hottest, then result[i] = 0
        constraints:
            - 1 <= n <= 1000
            - 1 <= temperatures[i] <= 100
        '''
        stack = []

        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            current = temperatures[i]

            while stack:
                value, index = stack.pop()

                if value < current:
                    result[index] = i - index
                else:
                    stack.append((value, index))
                    break
            
            stack.append((current, i))
        
        return result