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
        n = len(s)
        # if n % 2 == 1:
        #     return False

        stack = []
        opening = {'(', '[', '{'}
        closing = {')' : '(', ']' : '[', '}' : '{'}
        for i in range(n):
            char = s[i]

            if char in opening:
                stack.append(char)
            
            if char in closing:
                if not stack:
                    return False

                complement = stack.pop()

                if complement != closing[char]:
                    return False
        
        return not stack