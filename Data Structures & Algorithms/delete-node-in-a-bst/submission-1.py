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
            - root node of a bst
            - key to look for when deleting
        out:
            - delete the node w/the key from the BST
            - return the root node of the BST
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: 0 or 1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: 2 children
            min_node = self.getMinNode(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
        
    def getMinNode(self, root):
        """Helper to find the min node in a BST"""
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr