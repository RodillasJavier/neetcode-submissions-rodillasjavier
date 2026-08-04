# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        in:
            - root of a BST
            - val to insert into the tree
        out:
            - insert the val into the tree
            - return root node after the insertion
        constraints:
            - the new value DNE in the OG BST
            - 0 <= n <= 10,000
            - all node vals are unique
            - node vales can be positive or negative
        """
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


# time complexity: O(h)
# space complexity: O(h)
