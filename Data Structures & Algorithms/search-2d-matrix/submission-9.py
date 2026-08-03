class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        in:
            - m x n 2D matrix
            - int target
        out:
            - true iff target in matrix
            - false o/w
        constraints:
            - each row in matrix non-decr.
            - first int of each row is greater than the last int of prev row
            - 1 <= m, n <= 100
            - -10000 <= matrix[i][j], target <= 10000
        """
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols

            num = matrix[row][col]

            if num < target:
                low = mid + 1
            elif num > target:
                high = mid - 1
            else:
                return True
        
        return False


# time complexity: O(log m + log n)
# space complexity: O(1)
