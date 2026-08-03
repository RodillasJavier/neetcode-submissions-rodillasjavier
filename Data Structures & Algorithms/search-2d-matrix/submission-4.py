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
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        lr, hr = 0, num_rows - 1
        while lr <= hr:
            mid_row = (hr + lr) // 2

            small, big = matrix[mid_row][0], matrix[mid_row][-1]

            if big < target:
                lr = mid_row + 1
            elif small > target:
                hr = mid_row - 1
            else:
                break
        
        left, right = 0, num_cols - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid_row][mid] > target:
                right = mid - 1
            elif matrix[mid_row][mid] < target:
                left = mid + 1
            else:
                return True
        
        return False

# time complexity: O(log m + log n)
# space complexity: O(1)