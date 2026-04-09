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
        result = [0] * len(temperatures)

        for i, current in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current:
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
        
        return result

# Time Complexity: 
# Space Complexity: 