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
            j = i // 2

            if i % 2 == 0:
                output.append(output[j])
            else:
                output.append(output[j] + 1)
        
        return output