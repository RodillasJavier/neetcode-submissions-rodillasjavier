class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        in:
            - m x n matrix image
                - image[i][j] = pixel val of image
            - sr, sc origin pixel coords
            - color to change pixels to
        out:
            - modified image
        '''
        def dfs(row, col, color, target_color):
            # Verify in bounds
            ROWS, COLS = len(image), len(image[0])
            if not (0 <= row < ROWS) or not (0 <= col < COLS):
                return

            # Only change if color is not target
            if image[row][col] == color or image[row][col] != target_color:
                return

            image[row][col] = color

            dfs(row + 1, col, color, target_color)
            dfs(row - 1, col, color, target_color)
            dfs(row, col + 1, color, target_color)
            dfs(row, col - 1, color, target_color)
        
        target_color = image[sr][sc]
        dfs(sr, sc, color, target_color)
        return image

# time complexity: O(n * m)
# space complexity: O(1)