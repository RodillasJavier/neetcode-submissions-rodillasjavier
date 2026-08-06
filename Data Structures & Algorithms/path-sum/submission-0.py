# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        in:
            - root of a binary tree
            - int targetSum
        out:
            - true iff the tree has a root-to-lead path s.t.
                - sum(path) == targetSum
        constraints:
            - 0 <= n <= 5000
            - node.val can be pos or neg
            - targetSum can be pos or neg
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        if self.hasPathSum(root.left, targetSum - root.val):
            return True
        if self.hasPathSum(root.right, targetSum - root.val):
            return True

        return False


# time complexity: O(n)
# space complexity: O(h)
