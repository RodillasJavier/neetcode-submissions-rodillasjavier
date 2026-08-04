# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        in:
            - root of a bin tree
        out:
            - return inorder traversal of it's nodes' values
        constraints:
            - 0 <= n <= 100
            - node val can be pos or neg
        """
        res = []

        if not root:
            return res

        self.inorder(res, root)
        return res
    
    def inorder(self, res, root):
        if not root:
            return
        
        self.inorder(res, root.left)
        res.append(root.val)
        self.inorder(res, root.right)

# time complexity: O(n)
# space complexity: O(n)