# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        in:
            - integer array preorder
            - integer array inorder
        out:
            - rebuild bin tree from traversal arrays
            - return its root
        constraints:
            - both arrays same size
            - arays consist of unique values
            - 1 <= n <= 1000
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])

        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])

        return root