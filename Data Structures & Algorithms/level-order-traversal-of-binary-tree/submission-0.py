# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        in:
            - binary tree root
        out:
            - return level order traversal of the tree as a nested list
                - each sublist as values of nodes at a level (L -> R)
                - i.e. tree[0] is level 0, tree[1] is level 1, etc.
        constraints:
            - 0 <= n <= 1000
        """
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                current = queue.popleft()

                if not current:
                    continue

                level.append(current.val)

                queue.append(current.left)
                queue.append(current.right)
            
            if level:
                result.append(level)
        
        return result