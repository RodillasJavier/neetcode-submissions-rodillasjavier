class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        in:
            - integer n
        out:
            - count num of 1s in the bin representation of nums 0 .. n
            - return array 'output'
                - output[i] = num of 1s in bin representation
        constraints:
            - 0 <= n <= 1000
        """
        output = [0]

        for i in range(1, n + 1):
            offset = i // 2
            output.append(output[offset])

            if i % 2 != 0:
                output[-1] += 1

        return output


# time complexity: O(n)
# space complexity: O(n)
