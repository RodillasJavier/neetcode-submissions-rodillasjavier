class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        in:
            - int[] heights
            - heights[i] = height of a bar (wid = 1)
        out:
            - area of the largest rectangle that can be formed
        constraints:
            - 1 <= heights.length <= 1000
            - 0 <= heights[i] <= 1000
        '''
        stack = []  # Pairs: (start_index, height)
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                new_area = (i - index) * height
                max_area = max(max_area, new_area)

                start = index
            
            stack.append((start, h))
        
        return max_area

# Time complexity: O(n)
# Space complexity: O(n)