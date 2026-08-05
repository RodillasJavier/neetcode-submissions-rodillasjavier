# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        in:
            - root node of a BST
            - integer k
        out:
            - return the kth smallest value
        constraints:
            - n = number of nodes in the tree
            - 1 <= k <= n <= 1000
            - 0 <= node.val <= 1000
        """
        self.count, self.answer = 0, None

        self.inorder(root, k)

        return self.answer
    
    def inorder(self, root, k):
        if not root or self.count == k:
            return

        self.inorder(root.left, k)

        if self.count == k:
            return
        
        self.count += 1

        if self.count == k:
            self.answer = root.val
            return

        self.inorder(root.right, k)