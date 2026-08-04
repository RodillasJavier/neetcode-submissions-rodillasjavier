# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        in:
            - root of a binary tree
        out:
            - true iff height-balanced
                - bin tree s.t. height b/w subtrees is within 1
            - false o/w
        constraints:
            - 0 <= n <= 1000
        """
        if not root:
            return True
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root):
        if not root:
            return 0
        
        height = 1
        
        if root.left:
            height = max(self.getHeight(root.left) + 1, height)
        if root.right:
            height = max(self.getHeight(root.right) + 1, height)
        
        return height