class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        in:
            - str[] operations
            - operations[i]: ith operation to apply to the record
                - int x => record a new score of x
                - '+' => record a new score summing prev two
                - 'D' => record a new score double of prev
                - 'C' => invalidate prev score
        out:
            - sum of all the scores on the record after applying all operations
        """
        result = 0
        scores = []

        for operation in operations:
            if operation == '+':
                scores.append(scores[-1] + scores[-2])
            elif operation == 'D':
                scores.append(scores[-1] * 2)
            elif operation == 'C':
                scores.pop()
            else:
                scores.append(int(operation))
        
        return sum(scores)