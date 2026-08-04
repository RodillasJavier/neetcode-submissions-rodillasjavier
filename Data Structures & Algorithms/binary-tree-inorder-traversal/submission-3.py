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
        stack = []

        if not root:
            return res
        else:
            stack.append((root, False))

        while stack:
            curr, visited = stack.pop()

            if visited:
                res.append(curr.val)
            else:
                if curr.right:
                    stack.append((curr.right, False))
                
                stack.append((curr, True))

                if curr.left:
                    stack.append((curr.left, False))
        
        return res

# time complexity: O(n)
# space complexity: O(n)
