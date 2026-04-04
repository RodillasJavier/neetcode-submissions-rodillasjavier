class Solution:
    def isValid(self, s: str) -> bool:
        '''
        in:
            - str s
            - '(), [], {}'
        out: 
            - true if it is a valid string
                - open brackets closed by the same type
                - " " in the correct order
                - close brackets have corresponding open brackets
            - false o/w
        constraints: 
            - 1 <= n <= 1000
        '''
        if len(s) % 2 == 1:
            return False

        stack = []
        opening = {'(', '[', '{'}
        closing = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in opening:
                stack.append(char)
            
            if char in closing:
                if not stack:
                    return False

                if stack.pop() != closing[char]:
                    return False
        
        return not stack

# Time Complexity: O(n)
# Space Complexity: O(n)