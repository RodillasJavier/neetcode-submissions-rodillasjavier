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
        total = 0
        scores = []

        for operation in operations:
            if operation == '+':
                total += (scores[-1] + scores[-2])
                scores.append(scores[-1] + scores[-2])
            elif operation == 'D':
                total += (scores[-1] * 2)
                scores.append(scores[-1] * 2)
            elif operation == 'C':
                total -= scores.pop()
            else:
                scores.append(int(operation))
                total += int(operation)
        
        return total

# Time complexity: O(n)
# Space complexity: O(n)