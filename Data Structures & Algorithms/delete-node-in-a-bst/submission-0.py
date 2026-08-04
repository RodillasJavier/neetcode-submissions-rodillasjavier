# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        in:
            - root of a bst
            - key corresponding to the node we need to delete
        out:
            - delete the node w/the given key if present
            - return the root node of the BST
        constraints:
            - 0 <= n <= 10,000
            - node val can be pos or neg
            - all node vals are unique
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # case 1: 0 or 1 children
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # case 2: 2 children
        min_node = self.findMinNode(root.right)
        root.val = min_node.val
        root.right = self.deleteNode(root.right, min_node.val)

        return root
        

    def findMinNode(self, root):
        """Return the node with the minimum value in the BST"""
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr
