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
        
        height = self.getHeight(root)

        if height == -1:
            return False

        return True
        
    def getHeight(self, root):
        if not root:
            return 0
        
        left, right = 0, 0
        if root.left:
            left = self.getHeight(root.left)
        if root.right:
            right = self.getHeight(root.right)

        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        else:
            return max(left, right) + 1