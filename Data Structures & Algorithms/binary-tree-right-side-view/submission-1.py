# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        in:
            - root of a binary tree
        out:
            - return vals of nodes visible from the right side of the tree
        constraints:
            - 0 <= n <= 100
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            result.append(queue[0].val)

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)


        return result


# time complexity: O(n)
# space complexity: O(n)
