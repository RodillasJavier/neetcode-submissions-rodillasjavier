from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        in:
            - List[List[str]] board
        out:
            - true iff it is a valid sudoku
                - no dupes 1..9 in rows
                - no dupes 1..9 in cols
                - no dupes 1..9 in each 3x3 square
            - false o/w
        constraints:
            - board is 9 x 9 
            - each str is 1..9 or '.'
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                square_row = row // 3
                square_col = col // 3

                cell = board[row][col]
                if cell == '.':
                    continue

                if (
                    cell in rows[row] or 
                    cell in cols[col] or 
                    cell in squares[(square_row, square_col)]
                ):
                    return False
                
                rows[row].add(cell)
                cols[col].add(cell)
                squares[(square_row, square_col)].add(cell)
                
        return True