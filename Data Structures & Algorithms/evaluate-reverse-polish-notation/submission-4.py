class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        in: 
            - str[] tokens
            - represents a valid arithmetic expression in RPN
        out:
            - integer representing the evaluation of the expr
        constraints:
            - operators: +, -, * and /
            - division always truncates toward zero
            - 1 <= n <= 1000
            - ints from -100..100
        '''
        def solve(x, y, op):
            x, y = int(x), int(y)

            match op:
                case '+':
                    return x + y
                case '-':
                    return x - y
                case '*':
                    return x * y

            return x / y

        stack = []
        i = 0
        operators = {'+', '-', '*', '/'}
        while i < len(tokens):
            token = tokens[i]

            if token not in operators:
                stack.append(token)
            else:
                y = stack.pop()
                x = stack.pop()

                stack.append(solve(x, y, token))
            
            i += 1
        
        return int(stack[0])
            



'''
tokens=["4","13","5","/","+"]

(13, 5, /)
(4, 2, +)
'''