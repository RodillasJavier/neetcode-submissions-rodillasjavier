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

        candidate_row = -1

        low_row, high_row = 0, num_rows - 1
        while low_row <= high_row:
            mid_row = (high_row + low_row) // 2

            first_el, last_el = matrix[mid_row][0], matrix[mid_row][-1]

            if last_el < target:
                low_row = mid_row + 1
            elif first_el > target:
                high_row = mid_row - 1
            else:
                candidate_row = mid_row
                break

        if candidate_row == -1:
            return False

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
