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
        # inorder mapping
        val_to_inorder_idx = {value : idx for idx, value in enumerate(inorder)}
        preorder_idx = 0

        def build(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            mid = val_to_inorder_idx[root_val]

            preorder_idx += 1

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(preorder) - 1)


# time complexity: O(n)
# space complexity: O(n)
