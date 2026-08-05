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
        preorder_idx = 0
        inorder_idx = {val : idx for idx, val in enumerate(inorder)}

        def build(left, right):
            """
            helper to recursively build subtrees based on the L/R split of inorder 
            array
            """
            nonlocal preorder_idx

            if left > right:
                return

            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]

            preorder_idx += 1

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
    

# time complexity: O(n)
# space complexity: O(n)