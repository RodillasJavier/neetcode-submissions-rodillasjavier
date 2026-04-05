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
            match op:
                case '+':
                    return x + y
                case '-':
                    return x - y
                case '*':
                    return x * y
                case '/':
                    return int(x / y)

        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()

                stack.append(solve(x, y, token))
        
        return stack[0]

# Time Complexity: O(n)
# Space Complexity: O(n)