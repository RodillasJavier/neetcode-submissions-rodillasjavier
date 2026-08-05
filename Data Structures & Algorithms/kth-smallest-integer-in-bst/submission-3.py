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
        self.count, self.answer = 0, -1

        self.inorder(root, k)

        return self.answer

    def inorder(self, root, k):
        """
        inorder traverse of the BST starting from the root

        store the first k nodes in res in order to create a sorted array
        """
        if not root or self.count == k:
            return

        self.inorder(root.left, k)

        if self.count == k:
            return

        self.answer = root.val
        self.count += 1

        self.inorder(root.right, k)
