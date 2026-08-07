class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        in:
            - grid of integers
            - int sr, sc
            - int color
        out:
            - perform a flood fill on the image from (sr, sc)
            - return the modified image after performing the flood fill
        """
        ROWS, COLS = len(image), len(image[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        original_color = image[sr][sc]

        def dfs(sr, sc):
            if not 0 <= sr < ROWS or not 0 <= sc < COLS:
                return

            current_color = image[sr][sc]
            if current_color == color or current_color != original_color:
                return
            
            image[sr][sc] = color
            for dr, dc in DIRECTIONS:
                dfs(sr + dr, sc + dc)
            
        dfs(sr, sc)
        return image

# time complexity: O(r * c)
# space complexity: O(r * c)