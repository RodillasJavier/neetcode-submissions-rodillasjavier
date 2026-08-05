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

        queue = deque([root])
        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result