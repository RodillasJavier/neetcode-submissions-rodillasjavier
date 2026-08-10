"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        in:
            - node in an undirected graph
        out:
            - deep copy of the graph
        constraints:
            - nodes valued from 1 .. n
            - idx of each node in the adj list is the same as the nodes value
                - 1-indexed
            - input node = first node in the graph = 1
            - 0 <= n <= 100
            - 1 <= node.val <= 100
        """
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        if node is None:
            return None

        return dfs(node)


# time complexity: O(V + E)
# space complexity: O(V + E)
