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
        nodes = []

        self.inorder(nodes, root, k)

        return nodes[-1]

    def inorder(self, res, root, k):
        """
        inorder traverse of the BST starting from the root

        store the first k nodes in res in order to create a sorted array
        """
        if not root or len(res) == k:
            return

        self.inorder(res, root.left, k)

        if len(res) == k:
            return

        res.append(root.val)

        self.inorder(res, root.right, k)
