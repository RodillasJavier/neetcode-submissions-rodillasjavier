class NumMatrix:

    '''
    init obj w/int matrix containing the sum of each submatrix from bottom 
    right coord to origin (0, 0)

    time complexity: O(n^2)
    space complexity: O(n^2)
    '''
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (COLS + 1) for row in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0

            for c in range(COLS):
                prefix += matrix[r][c]
                self.sum_mat[r + 1][c + 1] = prefix + self.sum_mat[r][c + 1]

    '''
    Return sum of el in submatrix
    - row1, col1 => top left corner
    - row2, col2 => bot right corner

    time complexity: O(1)
    space complexity: O(1)
    '''
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottom_right = self.sum_mat[r2][c2]
        above = self.sum_mat[r1 - 1][c2]
        left = self.sum_mat[r2][c1 - 1]
        top_left = self.sum_mat[r1 - 1][c1 - 1]

        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)